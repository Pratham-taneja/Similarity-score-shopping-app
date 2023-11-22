from flask import Flask, jsonify, request
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import numpy as np

import os

# initializes model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# loads datset for comparison and encode it
path = 'https://drive.google.com/file/d/18hUp9j9d6CD3jdJwmDi6ZliJCSLLIV7b/view?usp=sharing'
df = pd.read_csv('https://drive.google.com/uc?export=download&id='+path.split('/')[-2])
embedding_database = model.encode(df['disc'].values, convert_to_tensor=True)

def get_score(sentence):

	# Analyse the text to generate similarity score
	# API for Google Cloud Development
	#	1. Encodes the input string/data/desripton.
	# 	2. Compares the string with existing data to generate score.
	# 	3. Returns list of top 10 products i.e. their similarity score and url/likt to product.

	urls = df['url'].values # List of urls

	# Encoding the input string
	embedding_current = model.encode(sentence, convert_to_tensor=True)

	# Generating similarity scores
	all_scores = util.pytorch_cos_sim(embedding_current, embedding_database).numpy().flatten() 

	data_li = []
	url_li=[]
	i=0
	while i<10:
		data_dict = {}
		cur_value = np.argmax(all_scores)

		data_dict['Score'] = str(all_scores[cur_value])
		data_dict['url'] = str(urls[cur_value])
		all_scores = np.delete(all_scores,cur_value)
		urls = np.delete(urls,cur_value)

		if (data_dict['url'] not in url_li):
			data_li.append(data_dict)
			i+=1
		elif len(url_li)>25:
			i=10

		url_li.append(data_dict['url'])

	return data_li

app = Flask(__name__)

# For handeling requests
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sentence = request.json

        if sentence is None or sentence == "":
            return jsonify({"error": "no file"})

        try:
            data = {"data": get_score(sentence['sentence'])}
            return jsonify(data)
    
        except Exception as e:
            return jsonify({"error": str(e)})

    return "OK"

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port = int(os.environment.get("PORT",8080)))
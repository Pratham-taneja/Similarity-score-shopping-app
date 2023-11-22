# Similarity Description
Compares the description with existing data to give top 10 similar products i.e. their similarity score and url to the products.

- Analyse the text to generate similarity score
- flask app for Google Cloud Development
	- 1. Encodes the input string/data/desripton.
	- 2. Compares the string with existing data to generate score.
	- 3. Returns list of top 10 products i.e. their similarity score and url/lint to product.

How to use ?
- Use the folder gcp_app to deploy model on GCP
- url_finder/url_finder.py driver code to get data from cloud
- scrapper contains ipynb file to scrap data from mintra and ajio and save it as csv
- other files
 	- url_finder/call_w_page gets the data and use chromium to display data/open all the url
 	- url_finder/main_locl_app.py is a script to deploy flask on local server

import requests
import pandas as pd
from selenium import webdriver


url = "https://ronak-12-bhatia-tnwuto4yoq-uc.a.run.app"
sentence = ["Olive green solid opaque Casual shirt ,has a spread collar, button placket, long roll-up sleeves, curved hem",
			"Black and green printed woven regular top, has a round neck, three-quarter sleeves, button closure"]

resp = requests.post(url, json={'sentence':sentence[1]})


result = pd.DataFrame(resp.json()['data'])

print(result)

PATH = " https://chromedriver.chromium.org/security-considerations"
driver = webdriver.Chrome(PATH)

for page in result['url'].values:
	driver.execute_script("window.open('"+page+"');")


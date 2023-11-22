import requests
import pandas as pd

url = "https://ronak-12-bhatia-tnwuto4yoq-uc.a.run.app"

# Description to compare
sentence = "Olive green solid opaque Casual shirt ,has a spread collar, button placket, long roll-up sleeves, curved hem"

resp = requests.post(url, json={'sentence':sentence})

result = pd.DataFrame(resp.json()['data'])

print(result)
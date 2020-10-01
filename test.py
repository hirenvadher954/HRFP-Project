import json
import requests

url = "http://127.0.0.1:5000/predict"
params = {
          "time" : 10,
          "ejection_fraction" : 22,
          "serum_creatinine" : 0.1,
          "age" : 35
          }

params = json.dumps(params)
loaded_params = json.loads(params)

response = requests.post(url, json=loaded_params)


# req = requests.post(url = url, data = params)
print(response.json())

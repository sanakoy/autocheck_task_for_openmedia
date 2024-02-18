
import requests

url = "http://parser-api.com/parser/gibdd_api/?key=149339b96d45b7c8cef65c0503b7ccbe&vin=JN1FANF15U0109775&vin=XTA217030C0372781&types=history,dtp,wanted,restrict"

response = requests.get(url)

print(response.status_code)  # Выводит код состояния HTTP, например, 200
print(response.json())
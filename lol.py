from kinopoisk_api import KP
import requests
import json
token1 = '6633c0f3-cf88-45db-b8cc-1e2064c62169'
id = '1143242'
# api = requests.get('https://kinopoiskapiunofficial.tech/api/v2.2/films/', headers={'Authorization': '6633c0f3-cf88-45db-b8cc-1e2064c62169'})
headers = {"X-API-KEY": token1}
request = requests.get('https://kinopoiskapiunofficial.tech/api/v2.2/films/' + id, headers=headers)
# api = requests.get('https://kinopoiskapiunofficial.tech/api/v2.2/films/')
kinopoisk = KP(token='6633c0f3-cf88-45db-b8cc-1e2064c62169')

print(request)
request_json = json.loads(request.text)
print(request_json)

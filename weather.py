"""Weather API"""
import requests
import os

key = "9cb4a71bd97b3ea953b6d69081e3acce"

request_parameters = {
    'access_key': key,
    'query': 'Warsaw'
}

response = requests.get(url="http://api.weatherstack.com/current", params=request_parameters)
response.raise_for_status()
# print(response.json())
city = response.json()['location']['name']
temperature = response.json()['current']['temperature']
observation_time = response.json()['current']['observation_time']

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print(city + ':\t' + str(temperature) + ' Celsius degrees, Observation time: ' + observation_time)

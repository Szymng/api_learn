"""Weather API"""
import requests

key = "9cb4a71bd97b3ea953b6d69081e3acce"

request_parameters = {
    'access_key': key,
    'query': 'Warsaw'
}

response = requests.get(url="http://api.weatherstack.com/current", params=request_parameters)
response.raise_for_status()
city = response.json()['request']['query']
temperature = response.json()['current']['temperature']

print(city + ':\t' + str(temperature) + ' Celsius degrees')

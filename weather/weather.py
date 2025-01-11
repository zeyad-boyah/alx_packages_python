import requests


weather = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")


if weather.status_code == 200:

    data = weather.json()
     
else:
    print(f"Failed to retrieve data. HTTP Status Code: {weather.status_code}")


print (data['current_weather'])
import requests
print("please enter your city:")
city_name = input()

# def weather(city_name):
    # api_key="a233dfc6876d52df778bd89303900472"
base_url= "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=a233dfc6876d52df778bd89303900472" 
    # complete_url = base_url + city_name + "&appid" + api_key +
response = requests.get(base_url)
data = response.json()
    
print(response)
print(data)
    
if data["cod"] != "404":
    y = data["main"]
    current_temperature = int(y["temp"])
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    
    z=data["weather"]
    weather_description = z[0]["description"]
    AI_brain = "Currently " + str(weather_description) + " - Temperature " + str(current_temperature) + " - Humidity " + str(current_humidity) + "%"
else:
    AI_brain = "Sorry, I can't find the city"
print(AI_brain)
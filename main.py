import discord
import requests
import json
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
dict1 = {}
def get_quote(city):
  url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
  querystring = {"q":city,"days":"3"}
  headers = {
	"X-RapidAPI-Key": "f77c5bde9bmsh775458a2f3f1651p175e25jsn8b6a2f52c501",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
  }
  response = requests.get(url, headers=headers, params=querystring)
  json_data = json.loads(response.text)
  return json_data

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/city'):
    city = message.content.split("/city ",1)[1]
    weather = get_quote(city)
    name = weather['location']['name']
    region = weather['location']['region']
    country = weather['location']['country']
    local_time = weather['location']['localtime']
    temp = weather['current']['temp_c']
    cond = weather['current']['condition']['text']
    wind_kph = weather['current']['wind_kph']
    feelslike_c = weather['current']['feelslike_c']
    date1 = weather['forecast']['forecastday'][0]['date']
    forecast1_maxtemp = weather['forecast']['forecastday'][0]['day']['maxtemp_c']
    forecast1_mintemp = weather['forecast']['forecastday'][0]['day']['mintemp_c']
    forecast1_rainchance = weather['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
    date2 = weather['forecast']['forecastday'][1]['date']
    forecast2_maxtemp = weather['forecast']['forecastday'][1]['day']['maxtemp_c']
    forecast2_mintemp = weather['forecast']['forecastday'][1]['day']['mintemp_c']
    forecast2_rainchance = weather['forecast']['forecastday'][1]['day']['daily_chance_of_rain']
    date3 = weather['forecast']['forecastday'][2]['date']
    forecast3_maxtemp = weather['forecast']['forecastday'][2]['day']['maxtemp_c']
    forecast3_mintemp = weather['forecast']['forecastday'][2]['day']['mintemp_c']
    forecast3_rainchance = weather['forecast']['forecastday'][2]['day']['daily_chance_of_rain']
    
    await message.channel.send("City: "+name+"\nRegion: " + region +     "\nCountry: " + country + "\nLocal Time: " + str(local_time) + "\nTemperature: " + str(temp)+"℃" + "\nCondition: "+ cond + "\nWind speed: "+str(wind_kph)+" kph"+"\nFeels like "+str(feelslike_c)+"℃"+"\nForecast:"+"\n"+str(date1)+": "+str(forecast1_maxtemp)+" ~ "+str(forecast1_mintemp)+", "+"Rain Chance: "+str(forecast1_rainchance)+"\n"+date2+": "+str(forecast2_maxtemp)+" ~ "+str(forecast2_mintemp)+", "+"Rain Chance: "+str(forecast2_rainchance)+"\n"+str(date3)+": "+str(forecast3_maxtemp)+" ~ "+str(forecast3_mintemp)+", "+"Rain Chance: "+str(forecast3_rainchance))

 
keep_alive()
client.run(os.environ['TOKEN'])

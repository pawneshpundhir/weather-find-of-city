# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

def store():
    outfiles=open('data.txt','a')
    flocation=(str(location))
    outfiles.write("city name: ")
    outfiles.write(flocation)

    ftemperature=(str(temp_city))
    outfiles.writelines("   current temperature: ")
    outfiles.write(ftemperature)
    
    fdesc=(str(weather_desc))
    outfiles.write("current weather desc: ")
    outfiles.write(fdesc)
    
    fhumiditiy=(str(hmdt))
    outfiles.write("current humidity: ")
    outfiles.write(fhumiditiy)
    
    fwindspeed=(str(wind_spd))
    outfiles.write("current wind speed: ")
    outfiles.write(fwindspeed)
    outfiles.close()
store()    
    
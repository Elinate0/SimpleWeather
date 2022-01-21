from tkinter import *
import requests
import json
import py_compile
master = Tk()
master.geometry("266x379")
master.resizable(False,False)

#IP Start
ip = requests.get('https://api.ipify.org').text
responseGeo = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey=API_KEY_HERE_IPGEOLOCATION&ip={ip}&fields=geo')
result = responseGeo.content.decode()
result = json.loads(result)
# print(result["city"])
#IP End


# Weather Start
weatherTypes = ['clear sky', 'few clouds','overcast clouds', 'scattered clouds', 'broken clouds', 'shower rain', 'rain', 'thunderstorm','light snow', 'snow','mist']
##You can change it to whichever language you want to translate from here.
weatherTurkish = ['Güneşli', 'Az Bulutlu','Çok Bulutlu(Kapalı)', 'Alçak Bulutlu', 'Yer Yer Açık Bulutlu', 'Sağanak Yağmurlu', 'Yağmurlu', 'Gök Gürültülü Fırtına', 'Hafif Karlı', 'Karlı', 'Puslu']
##
city = result["city"]
apiGeo = 'API_KEY_HERE_OPENWEATHERMAP'
responseWeather = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiGeo}')
weatherData = responseWeather.json()
temperature = int(weatherData["main"]["feels_like"] - 273.15)
weatherDes = weatherData["weather"][0]["description"]
countryTag = weatherData["sys"]["country"]
state = weatherData["name"]
for i in range(len(weatherTypes)):
    if weatherDes == weatherTypes[i]:
        weatherDes = weatherTurkish[i]
#Weather End


#GUI Start
stateLabel = Label(master, font = ("Arial", 15) ,fg = "#1A82A9" ,text="{}".format(state))
stateLabel.grid(row = 1, column = 1, columnspan = 10, rowspan = 10, padx = 100, pady = 30)
countryLabel = Label(master, font = ("Arial", 10) ,fg = "#1A82A9" ,text="{}".format(countryTag))
countryLabel.grid(row = 1, column = 1, columnspan = 10, rowspan = 20, padx = 100, pady = 60)
temperatureLabel = Label(master, font = ("Arial", 25) ,fg = "#1A82A9" ,text="{}°".format(temperature))
temperatureLabel.grid(row = 2, column = 2, columnspan = 100, rowspan = 100, padx = 100, pady = 250)
dayLabel = Label(master, font = ("Arial", 10) ,fg = "#1A82A9" ,text="Bugün".format(temperature))
dayLabel.grid(row = 2, column = 2, columnspan = 100, rowspan = 110, padx = 110, pady = 300)
#GUI End

master.mainloop()
py_compile.compile("main.py")

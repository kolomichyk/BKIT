import requests
import config

s_city = 'Moscow'
id_city = 524901

def Get_Weather_Today():
    global s_city
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                    params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': config.WEATHER_TOKEN})

        data = res.json()
        return("{}; Температура: {}; Ощущается: {}; Минимальная температура: {}; Максимальная температура: {} Давление: {}, Скорость ветра: {}"\
            .format(data['list'][0]['weather'][0]['description'], data['list'][0]['main']['temp'], data['list'][0]['main']['feels_like'], data['list'][0]['main']['temp_min'],\
                data['list'][0]['main']['temp_max'], data['list'][0]['main']['pressure'], data['list'][0]['wind']['speed']))
    except Exception as e:
        return("Exception (find):", e)

def Get_Weather_Five_Day():
    global id_city
    s = ''
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                            params={'id': id_city, 'units': 'metric', 'lang': 'ru', 'APPID': config.WEATHER_TOKEN})
        data = res.json()
        for i in data['list']:
            s += i['dt_txt'] + '{0:+3.0f}'.format(i['main']['temp']) + ' ' + i['weather'][0]['description'] +'\n'
    except Exception as e:
        s += "Exception (forecast)"
    return s

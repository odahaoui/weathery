import datetime
import string
import requests
from flask import Flask, render_template, request
from datetime import date 


app = Flask(__name__)
app.config.from_object('config')

url = 'https://api.thingspeak.com/channels/1743324/feeds.json'
url2 =requests.get('https://api.openweathermap.org/data/2.5/weather?appid=97bd0d9a205165f3e7864984fd0a8814&q=Marrakech,MA&units=imperial%27')
@app.route('/')
def home():
    request = requests.get(url, params={'results': "2"})
    if request.status_code == 200:
        data = request.json()
        data2 = url2.json()
    else:
        return 0
    pressure = float(data2['main']['pressure'])
    wind_speed = float(data2['wind']['speed'])
    visi = round(data2['visibility'])
    tempa = float(data.get('feeds')[0].get('field1'))
    humi = float(data.get('feeds')[0].get('field2'))
    dateTimeObj = datetime.datetime.now()
    dateObj = dateTimeObj.date()
    time = dateTimeObj.strftime("%H:%M")

    return render_template('pages/placeholder.home.html',visi=visi, tempa=tempa,wind_speed= wind_speed, humi=humi, time=time, pressure = pressure)


@app.route('/history')
def history():
    return render_template('pages/placeholder.about.html')


if __name__ == '__main__':
    app.run(ssl_context='adhoc')

 
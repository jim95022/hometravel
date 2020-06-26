from flask import Flask, render_template
from random import choice
from cities import cities
import requests, json

app = Flask(__name__)

class city():
    def __init__(self):
        name = 'None'
        content = 'None'
        lat = 'None'
        lng = 'None'
        photo = 'None'

@app.route('/')
def map():
    city.name = choice(cities)[1]
    url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={city.name}&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyC9XrXe1rrRiJsBU-ZwalbqCtz2Gy69ZmI'
    city.content = json.loads(requests.get(url).text)
    city.lat = city.content['candidates'][0]['geometry']['location']['lat']
    city.lng = city.content['candidates'][0]['geometry']['location']['lng']
    photo_ref = city.content['candidates'][0]['photos'][0]['photo_reference']
    city.photo = f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_ref}&key=AIzaSyC9XrXe1rrRiJsBU-ZwalbqCtz2Gy69ZmI'

    return render_template('map.html', city=city)

if __name__ == "__main__":
    app.run()
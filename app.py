import os 
from random import choice
import requests, json

from flask import Flask, render_template

from cities import cities


GOOGLE_MAPS_API = os.environ['GOOGLE_MAPS_API']

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
    url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={city.name}&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={GOOGLE_MAPS_API}'
    city.content = json.loads(requests.get(url).text)
    city.lat = city.content['candidates'][0]['geometry']['location']['lat']
    city.lng = city.content['candidates'][0]['geometry']['location']['lng']
    photo_ref = city.content['candidates'][0]['photos'][0]['photo_reference']
    city.photo = f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_ref}&key={GOOGLE_MAPS_API}'

    return render_template('map.html', city=city)

if __name__ == "__main__":
    app.run()
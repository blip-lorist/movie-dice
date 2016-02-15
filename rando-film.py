from flask import Flask, jsonify
import os
from os.path import join, dirname
from dotenv import load_dotenv
import urllib
import csv
import random

app = Flask(__name__)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

@app.route('/rando-film/')
def hello_world():
    
    # download google spreadsheet 
    film_url = os.environ['FILM_URL']
    urllib.urlretrieve(film_url, 'films.csv')

    recs = []
    # randomly select a film
    with open('films.csv') as film_csv:
        reader = csv.reader(film_csv) 
        next(reader, None) # skip header

        for line in reader:
            recs.append(line[0])

    choice = random.choice(recs)
    # send it back via json
    return jsonify(response_type='in_channel', text=choice) 

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

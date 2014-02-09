from flask import Flask
from flask import render_template
import json
import pymongo
import db

application = Flask(__name__)
application.config.from_object('config') #Need to have a secret key for WTForms

@application.route('/') #Simple page, serves up index with a WTForm
def index():
	return render_template('index.html')

@application.route('/about')
def about():
	return render_template('about.html')

@application.route('/songs/<year>', methods=['GET']) #Gets the user some people to follow
def get_songs_from_handle(year):
	songs = db.get_lyrics_by_year(year)
	return json.dumps(songs)

if __name__ == '__main__':
	application.debug = True
	application.run(host='0.0.0.0', debug=True)

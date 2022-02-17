from cgitb import html
import requests
from bs4 import BeautifulSoup
import flask
from flask import request

URL = 'http://mathanosto.top/movie.php?imdbid=' + 'tt10733228' + '&cat=' + 'Bollywood'
html_text = requests.get(URL).text
soup = BeautifulSoup(html_text, 'lxml')
moviePlayURL  = soup.find('a', class_='btn-element btn btn-fullcolor btn-block btn-fullwidth')['href']


app = flask.Flask(__name__)

@app.route('/' , methods=['GET'])
def home():
    arg  = request.args['arg1']
    return moviePlayURL


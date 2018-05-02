from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import json

home = Blueprint('monitor', __name__ )

#@monitor.route('/', defaults={'page': 'home'})
#@monitor.route('/<page>')
@home.route('/')
def show():
    #try:
        return render_template('pages/home.html' )
    #except TemplateNotFound:
        #abort(404)

@home.route('/test')
def test():
        return "hola"

@home.route('/sites')
def sites():
	data = json.load(open('sites.json'))
	return data

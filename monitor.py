from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import json

monitor = Blueprint('monitor', __name__,
                        template_folder='templates')

#@monitor.route('/', defaults={'page': 'home'})
#@monitor.route('/<page>')
@monitor.route('/')
def show():
    try:
        return render_template('pages/home.html' )
    except TemplateNotFound:
        abort(404)

@monitor.route('/sites')
def sites():
	data = json.load(open('sites.json'))
	return data
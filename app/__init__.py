from flask import Flask

# Initialize application
app = Flask(__name__, static_folder='static' , template_folder='templates')

# Register blue prints
from app.modules.home.ctl import home

app.register_blueprint(home,url_prefix='/monitor')

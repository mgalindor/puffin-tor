from flask import Flask

## Import of routes
from monitor import monitor


app = Flask(__name__)
app.register_blueprint(monitor)


if __name__ == "__main__":
    app.run()
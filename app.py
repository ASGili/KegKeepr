from flask import Flask

app = Flask(__name__)

from controllers import beer_controller
from controllers import keg_controller

if __name__ == "__main__":
    app.run(debug=True)
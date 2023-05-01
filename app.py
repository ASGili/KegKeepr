from flask import Flask

app = Flask(__name__)

from controllers.beer_controller import beer_blueprint
from controllers.keg_controller import keg_blueprint

app.register_blueprint(keg_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
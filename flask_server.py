from flask import Flask, render_template
import app

flask_app = Flask(__name__)


@flask_app.route("/")
def homepage():
  return "Home route"

@flask_app.route("/about")
def about():
  app.rgb2gray(app.loadimag())
  return "About Route"

if __name__ == "__main__":
  flask_app.run(debug=True, port=5000)
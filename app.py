from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home.html")


app.run(port=8000)

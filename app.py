from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html")


@app.route("/market")
def market():
    items = [
        {"id": 1, "name": "Apple", "price": 2000},
        {"id": 2, "name": "Dell", "price": 1300},
        {"id": 3, "name": "Microsoft", "price": 1000},
    ]

    return render_template("market.html", items=items)


app.run(port=8000)

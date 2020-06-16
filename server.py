from flask import Flask
import random
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/roll-dice/<int:n>")
def roll_dice_1(n):
    n_1 = sum([random.randint(1, 2) for i in range(n)])
    n_2 = random.randint(1, 6)
    n_3 = random.randint(1, 6)
    n_4 = random.randint(1, 6)
    return render_template("roll-dice.html", n_1 = n_1, n_2=n_2, n_3 = n_3, n_4=n_4)

@app.route("/hello/<name>")
def sayhi(name):
    return f"Hello, {name.title()}"

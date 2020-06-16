from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World"

@app.route("/roll-dice")
def roll_dice_1():
    n_1 = random.randint(1, 6)
    n_2 = random.randint(1, 6)
    n_3 = random.randint(1, 6)
    return f"Our random numbers are {str(n_1)}, {str(n_2)} and {str(n_3)}"

@app.route("/hello/<name>")
def sayhi(name):
    return f"Hello, {name.title()}"
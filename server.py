from flask import Flask
import random
from flask import render_template
from flask import request
from model import predict

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

@app.route("/my-first-form")
def my_first_form():
    return render_template("my-first-form.html")

@app.route("/make-greeting", methods=["POST"])
def handle_form_submission():
    name = request.form["name"]
    title = request.form["title"]

    greeting = "Hello, "

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template("greeting-result.html", greeting = greeting)

@app.route("/is-spam")
def spam_form():
    return render_template("spam-input-form.html")

@app.route("/spam-result", methods=["POST"])
def spam_result():
    text = request.form["message"]
    comment = f"Your text is {predict(text)}"

    return render_template("spam-result.html", text= text, comment = comment)

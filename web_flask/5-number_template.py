#!/usr/bin/python3
""" Flask application"""

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """ show hello hbnb"""
    return 'Hello HBNB!'


@app.route("/hbnb")
def hbnb():
    """ show hbnb"""
    return 'HBNB'


@app.route("/c/<text>")
def c(text):
    """ display text"""
    return f'C {text.replace("_", " ")}'


@app.route("/python")
@app.route("/python/<text>")
def python(text="is cool"):
    """ diplay text"""
    return f"Python {text.replace("_"," ")}"


@app.route('/number/<int:n>')
def num(n):
    """ diplay integer """
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """ diplay template """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

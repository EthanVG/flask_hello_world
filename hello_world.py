from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hi_person(name):
    html ="""
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten. Awww...
        <p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
    
@app.route("/jedi/<fn>/<ln>")
def jedi_name(fn, ln):
    first = fn
    last = ln
    
    jedi = last[:3] + first[:2]
    
    return("Hello {}!".format(jedi))
    
if __name__ == "__main__":
    app.run(host=environ['IP'], port=int(environ['PORT']))
from flask import Flask
import json
from config import dev, sum

app = Flask(__name__)


@app.get("/")
def hello():
    return "Hello from Flask!"

@app.get("/test")
def test():
    return "Test page"

@app.get("/about")
def about_me():
    return "Guillermo Escobar"


#########API METHODS#########


@app.get("/api/developer")
def developer():
    return json.dumps(dev)



@app.get("/api/sum")
def simple_sum():
    key = sum(21, 21)
    return json.dumps(key)



app.run(debug=True)
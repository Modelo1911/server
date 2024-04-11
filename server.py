from flask import Flask, request
import json
from config import dev, sum
from data import catalog
from flask_cors import CORS 


app = Flask(__name__)
CORS(app) # Warning! this will disable CORS policy


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

@app.get("/api/products")
def get_catalog():
    return json.dumps(catalog)

@app.post("/api/products")
def save_product():
    prod = request.get_json()
    catalog.append(prod)

    return json.dumps(prod)

app.run(debug=True)
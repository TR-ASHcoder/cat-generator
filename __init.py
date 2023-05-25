from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

def get_cat():
  url = "https://some-random-api.com/animal/cat"
  response = json.loads(requests.request("GET", url).text) 
  image = response['image']
  fact = response['fact']
  return image, fact
  
@app.route('/')
def index():
    cat, fact = get_cat()
    return render_template("index.html", cat = cat, fact = fact)
 
app.run(host="0.0.0.0", port=8080)



from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    products = ['Ciabatta', 'Baguete', 'Pretzel', 'Pao Frances']
    return render_template("index.html", products=products)
from flask import Flask
from products import products

app = Flask(__name__)

@app.route("/products")
def listProducts():
    return "Productos"

if __name__ == "__main__":
    app.run(debug=True, port=4000)

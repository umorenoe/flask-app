from flask import Flask, jsonify
from products import products

app = Flask(__name__)

@app.route('/test')
def test():
    return 'Productos'

@app.route('/test-json')
def testJson():
    return jsonify({'name': 'Productos'})

@app.route('/products')
def productList():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, port=4000)

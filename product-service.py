from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample product data (you can load this from a file or database)
products = {
    "1": {"name": "tuti", "description": "Description of Product A", "price": 10, "inventory": 100},
    "2": {"name": "fruiti", "description": "Description of Product B", "price": 20, "inventory": 50},
}

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    return "Product not found", 404

if __name__ == '__main__':
    app.run(debug=True)

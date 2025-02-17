from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Mock product data
product = {
    "id": 1,
    "name": "Wireless Bluetooth Headphones",
    "description": "Experience crystal-clear sound with these wireless headphones. Perfect for music lovers and professionals alike.",
    "price": 99.99,
    "images": [
        "https://via.placeholder.com/600x400",
        "https://via.placeholder.com/600x400",
        "https://via.placeholder.com/600x400"
    ],
    "rating": 4.5
}

@app.route("/")
def product_detail():
    # Initialize cart in session if not already present
    if "cart" not in session:
        session["cart"] = []
    return render_template("product_detail.html", product=product)

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    # Add product to cart
    cart_item = {
        "id": product["id"],
        "name": product["name"],
        "price": product["price"]
    }
    session["cart"].append(cart_item)
    session.modified = True  # Mark session as modified
    return redirect(url_for("product_detail"))

@app.route("/cart")
def view_cart():
    # Display cart items
    cart_items = session.get("cart", [])
    total_price = sum(item["price"] for item in cart_items)
    return render_template("cart.html", cart_items=cart_items, total_price=total_price)

if __name__ == "__main__":
    app.run(debug=True)
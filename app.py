from flask import Flask, render_template, redirect, url_for, session, request
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Sample data for demonstration with 5 restaurants, each with appropriate descriptions
restaurants = {
    1: {'name': 'The Italian Kitchen', 'description': 'Authentic Italian cuisine with a variety of pizzas, pastas, and fresh salads.', 'menu': [
        {'id': 1, 'name': 'Pizza Margherita', 'price': 12},
        {'id': 2, 'name': 'Classic Burger', 'price': 8},
        {'id': 3, 'name': 'Penne Alfredo', 'price': 10},
        {'id': 4, 'name': 'Caesar Salad', 'price': 7},
        {'id': 5, 'name': 'Minestrone Soup', 'price': 5}
    ]},
    2: {'name': 'Sushi House', 'description': 'Fresh sushi, ramen, and tempura from the heart of Japan, crafted with the finest ingredients.', 'menu': [
        {'id': 6, 'name': 'Sushi Platter', 'price': 15},
        {'id': 7, 'name': 'Ramen Noodles', 'price': 12},
        {'id': 8, 'name': 'Tempura', 'price': 10},
        {'id': 9, 'name': 'Miso Soup', 'price': 5},
        {'id': 10, 'name': 'Udon Noodles', 'price': 11}
    ]},
    3: {'name': 'Mexican Fiesta', 'description': 'Delightful Mexican dishes bursting with bold flavors and fresh ingredients.', 'menu': [
        {'id': 11, 'name': 'Tacos', 'price': 9},
        {'id': 12, 'name': 'Burrito', 'price': 10},
        {'id': 13, 'name': 'Quesadilla', 'price': 8},
        {'id': 14, 'name': 'Loaded Nachos', 'price': 7},
        {'id': 15, 'name': 'Guacamole', 'price': 5}
    ]},
    4: {'name': 'Burger Palace', 'description': 'Juicy, handcrafted burgers made with premium ingredients. The perfect stop for burger lovers!', 'menu': [
        {'id': 16, 'name': 'Cheeseburger', 'price': 8},
        {'id': 17, 'name': 'Chicken Burger', 'price': 9},
        {'id': 18, 'name': 'Veggie Burger', 'price': 7},
        {'id': 19, 'name': 'Double Cheeseburger', 'price': 11},
        {'id': 20, 'name': 'Fries', 'price': 3}
    ]},
    5: {'name': 'Grill Master BBQ', 'description': 'Smoky and savory BBQ delights, including ribs, grilled chicken, and delicious sides.', 'menu': [
        {'id': 21, 'name': 'Grilled Chicken', 'price': 13},
        {'id': 22, 'name': 'BBQ Ribs', 'price': 16},
        {'id': 23, 'name': 'Pulled Pork Sandwich', 'price': 10},
        {'id': 24, 'name': 'Grilled Veggies', 'price': 7},
        {'id': 25, 'name': 'Coleslaw', 'price': 4}
    ]},
    6: {'name': 'Vegan Delights', 'description': 'A haven for vegans! Fresh, plant-based meals that are delicious, healthy, and sustainable.', 'menu': [
        {'id': 26, 'name': 'Vegan Burger', 'price': 9},
        {'id': 27, 'name': 'Quinoa Salad', 'price': 8},
        {'id': 28, 'name': 'Tofu Stir-fry', 'price': 10},
        {'id': 29, 'name': 'Vegan Tacos', 'price': 7},
        {'id': 30, 'name': 'Fruit Bowl', 'price': 5}
    ]}
}

cart = []

@app.route('/')
def index():
    return render_template('index.html', restaurants=restaurants)

@app.route('/restaurants/<int:restaurant_id>/menu')
def menu(restaurant_id):
    restaurant = restaurants.get(restaurant_id)
    if restaurant:
        return render_template('menu.html', restaurant=restaurant)
    return "Restaurant not found", 404

@app.route('/cart/add/<int:item_id>')
def add_to_cart(item_id):
    # Add item to cart (dummy logic)
    cart.append(item_id)
    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    # Display the cart with a summary
    items_in_cart = [item for rest in restaurants.values() for item in rest['menu'] if item['id'] in cart]
    total = sum(item['price'] for item in items_in_cart)
    return render_template('cart.html', cart=items_in_cart, total=total)

@app.route('/cart/remove/<int:item_id>')
def remove_from_cart(item_id):
    # Remove item from cart (dummy logic for now)
    global cart
    cart = [item for item in cart if item != item_id]
    return redirect(url_for('view_cart'))


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        address = request.form['address']
        # Process order (dummy logic)
        session['order'] = {'cart': cart, 'address': address}
        return redirect(url_for('order_confirmation'))
    return render_template('checkout.html')

@app.route('/order/confirmation')
def order_confirmation():
    # Check if there's an order in the session
    order = session.get('order')
    if order:
        return render_template('order_confirmation.html')
    return "No order found", 404


if __name__ == '__main__':
    app.run(debug=True)

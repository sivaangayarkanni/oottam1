from flask import Flask, render_template, session, redirect, url_for, request, jsonify, flash
from config import Config
from models import db, Product
from forms import ContactForm, CheckoutForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def create_sample_products():
    if Product.query.count() == 0:
        products = [
            Product(
                name='Multipurpose Flour - Original',
                slug='multipurpose-flour-original',
                description='Our signature multipurpose flour crafted from the finest wheat, milled using traditional methods to preserve natural nutrition. Perfect for everyday meals that your family will love.',
                short_description='Our signature flour for everyday meals',
                price=249,
                original_price=299,
                type='multipurpose',
                flavor='original',
                image='flour-original',
                ingredients='Whole Wheat Flour (90%), Rice Flour (5%), Bengal Gram Flour (5%)\n\nNo preservatives. No artificial additives. 100% natural.',
                how_to_use='1. Take required amount of flour\n2. Add water gradually\n3. Knead to desired consistency\n4. Use for roti, dosa, porridge, or snacks',
                use_cases='Roti|Dosa|Porridge|Snacks|Quick Meals',
                benefits='High in fiber|Multiple use cases|Quick preparation|Traditional taste'
            ),
            Product(
                name='Multipurpose Flour - Multigrain',
                slug='multipurpose-flour-multigrain',
                description='A powerhouse of nutrition combining six grains. Rich in fiber and protein, this multigrain flour supports digestive health while delivering authentic taste.',
                short_description='Power-packed nutrition from six grains',
                price=299,
                original_price=349,
                type='multipurpose',
                flavor='multigrain',
                image='flour-multigrain',
                ingredients='Wheat Flour (40%), Ragi Flour (15%), Jowar Flour (15%), Bajra Flour (10%), Rice Flour (10%), Chana Flour (10%)\n\nNo preservatives. No artificial additives.',
                how_to_use='1. Mix flour well\n2. Add water as needed\n3. Knead into soft dough\n4. Cook as usual',
                use_cases='Roti|Dosa|Uttapam|Snacks|Breakfast',
                benefits='High protein|High fiber|6-grain nutrition|Heart healthy'
            ),
            Product(
                name='Ragi Flour - Instant',
                slug='ragi-flour-instant',
                description='Nature\'s superfood in its purest form. Ragi is rich in calcium and iron, making it perfect for growing children and health-conscious adults.',
                short_description='Nutrient-rich superfood flour',
                price=179,
                original_price=None,
                type='instant',
                flavor='ragi',
                image='flour-ragi',
                ingredients='Organic Finger Millet (Ragi) Flour (100%)\n\nNo preservatives. No artificial additives. Single ingredient.',
                how_to_use='1. Mix 2-3 tbsp with water or milk\n2. Boil for 5 minutes\n3. Add jaggery for sweetness\n4. Serve warm',
                use_cases='Porridge|Roti|Breakfast|Health Drink|Desserts',
                benefits='High calcium|High iron|Natural energy|Gluten-free'
            ),
            Product(
                name='Rice Flour - Fine',
                slug='rice-flour-fine',
                description='Stone-ground fine rice flour ideal for traditional recipes like paniyaram, neer dosa, and crispy snacks. Light, easy to digest, and naturally gluten-free.',
                short_description='Traditional recipes made easy',
                price=169,
                original_price=199,
                type='multipurpose',
                flavor='rice',
                image='flour-rice',
                ingredients='Organic Rice Flour (100%)\n\nNo preservatives. No artificial additives. Single ingredient.',
                how_to_use='1. Mix with water to desired consistency\n2. Add salt and spices\n3. Ferment if needed\n4. Cook as per recipe',
                use_cases='Dosa|Snacks|Fryums| desserts|Batters',
                benefits='Gluten-free|Light texture|Easy digest|Low allergy'
            ),
            Product(
                name='Kitchen Special Combo',
                slug='kitchen-special-combo',
                description='The complete kitchen solution. Four essential flours in one pack - Original, Multigrain, Ragi, and Rice. Everything you need for a week of healthy meals.',
                short_description='Four flours. Endless possibilities.',
                price=699,
                original_price=849,
                type='combo',
                flavor='original',
                image='flour-combo',
                ingredients='Set includes: Original Flour (1kg), Multigrain Flour (500g), Ragi Flour (500g), Rice Flour (500g)\n\nNo preservatives. No artificial additives.',
                how_to_use='Use each flour according to its specific instructions. Mix and match for creative recipes.',
                use_cases='All recipes|Variety meals|Experiments|Gifts',
                benefits='Best value|4-in-1|Variety|Perfect for families'
            ),
            Product(
                name='Breakfast Mix - Instant',
                slug='breakfast-mix-instant',
                description='Start your morning right with our ready-to-cook breakfast mix. Just add water and cook for nutritious dosas or pancakes in under 5 minutes.',
                short_description='Healthy breakfast in 5 minutes',
                price=189,
                original_price=None,
                type='instant',
                flavor='original',
                image='flour-breakfast',
                ingredients='Rice Flour (60%), Urad Dal Flour (20%), Wheat Flour (15%), Salt, Fenugreek (5%)\n\nNo preservatives. No artificial additives.',
                how_to_use='1. Mix 1 cup flour with 1 cup water\n2. Let rest for 5 minutes\n3. Cook on hot tawa like regular dosa\n4. Serve with favorite sides',
                use_cases='Dosa|Pancakes|Upma|Breakfast|Snacks',
                benefits='Quick prep|High protein|Healthy start|Zero effort'
            )
        ]
        for p in products:
            db.session.add(p)
        db.session.commit()

@app.route('/')
def index():
    featured = Product.query.limit(3).all()
    return render_template('index.html', featured=featured)

@app.route('/products')
def products():
    product_type = request.args.get('type', 'all')
    flavor = request.args.get('flavor', 'all')
    
    query = Product.query
    if product_type != 'all':
        query = query.filter_by(type=product_type)
    if flavor != 'all':
        query = query.filter_by(flavor=flavor)
    
    all_products = query.all()
    return render_template('products.html', products=all_products, current_type=product_type, current_flavor=flavor)

@app.route('/product/<slug>')
def product(slug):
    product = Product.query.filter_by(slug=slug).first_or_404()
    related = Product.query.filter(Product.type == product.type, Product.id != product.id).limit(3).all()
    return render_template('product.html', product=product, related=related)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', {})
    if not cart_items:
        return render_template('cart.html', products=[], total=0)
    
    products = []
    total = 0
    for product_id, quantity in cart_items.items():
        product = Product.query.get(int(product_id))
        if product:
            products.append({
                'product': product,
                'quantity': quantity,
                'item_total': product.price * quantity
            })
            total += product.price * quantity
    
    return render_template('cart.html', products=products, total=total)

@app.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = int(request.args.get('quantity', 1))
    
    cart = session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] += quantity
    else:
        cart[str(product_id)] = quantity
    
    session['cart'] = cart
    flash(f'Added {product.name} to cart!', 'success')
    return redirect(request.referrer or url_for('products'))

@app.route('/update-cart/<int:product_id>')
def update_cart(product_id):
    action = request.args.get('action', 'set')
    quantity = int(request.args.get('quantity', 1))
    
    cart = session.get('cart', {})
    product_key = str(product_id)
    
    if product_key in cart:
        if action == 'increase':
            cart[product_key] += 1
        elif action == 'decrease':
            cart[product_key] = max(0, cart[product_key] - 1)
        elif action == 'set':
            cart[product_key] = max(0, quantity)
        elif action == 'remove':
            cart.pop(product_key, None)
    
    if cart[product_key] == 0:
        cart.pop(product_key, None)
    
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart_items = session.get('cart', {})
    if not cart_items:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('products'))
    
    products = []
    total = 0
    for product_id, quantity in cart_items.items():
        product = Product.query.get(int(product_id))
        if product:
            products.append({
                'product': product,
                'quantity': quantity,
                'item_total': product.price * quantity
            })
            total += product.price * quantity
    
    form = CheckoutForm()
    if form.validate_on_submit():
        flash('Order placed successfully! (This is a demo - no real payment)', 'success')
        session.pop('cart', None)
        return redirect(url_for('index'))
    
    return render_template('checkout.html', form=form, products=products, total=total)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Message sent successfully! We\'ll get back to you soon.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

@app.context_processor
def cart_count():
    cart = session.get('cart', {})
    count = sum(cart.values()) if cart else 0
    return dict(cart_count=count)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_sample_products()
    app.run(debug=True)
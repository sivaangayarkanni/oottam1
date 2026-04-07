from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    short_description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    original_price = db.Column(db.Float, nullable=True)
    type = db.Column(db.String(50), nullable=False)
    flavor = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    how_to_use = db.Column(db.Text, nullable=False)
    use_cases = db.Column(db.Text, nullable=False)
    benefits = db.Column(db.Text, nullable=False)
    in_stock = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'description': self.description,
            'short_description': self.short_description,
            'price': self.price,
            'original_price': self.original_price,
            'type': self.type,
            'flavor': self.flavor,
            'image': self.image,
            'ingredients': self.ingredients,
            'how_to_use': self.how_to_use,
            'use_cases': self.use_cases,
            'benefits': self.benefits,
            'in_stock': self.in_stock
        }
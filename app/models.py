from app import db

class RawMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('Supplier.id'), nullable=True)
    # This is a many-to-many relationship
    recipes = db.relationship('Recipe', secondary='recipe_raw_material', lazy='subquery', backref=db.backref('raw_materials', lazy=True))
    def __repr__(self):
        return f'<RawMaterial {self.name}>'
    
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    # This is a many-to-many relationship
    raw_materials = db.relationship('RawMaterial', secondary='recipe_raw_material', lazy='subquery', backref=db.backref('recipes', lazy=True))

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    # This is a one-to-many relationship
    raw_materials = db.relationship('RawMaterial', backref='supplier', lazy=True)
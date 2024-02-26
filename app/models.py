from app import db

class RawMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=True)

    def __repr__(self):
        return f'<RawMaterial {self.name}>'
    
class supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    # This is a one-to-many relationship
    raw_materials = db.relationship('RawMaterial', backref='supplier', lazy=True)
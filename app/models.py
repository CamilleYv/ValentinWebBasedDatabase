from app import db

class RawMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=True)
    supplier = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return f'<RawMaterial {self.name}>'
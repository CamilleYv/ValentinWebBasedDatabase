from sqlalchemy import Integer, String, Column, ForeignKey,Float, Table,event
from sqlalchemy.orm import relationship, backref
from extension import db

class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    name = Column(String(128), unique=True, nullable=False)
    price = Column(Integer, nullable=True)
    __mapper_args__ = {
        'polymorphic_identity': 'ingredient',
        'polymorphic_on': type
    }

class RawMaterial(Ingredient):
    __tablename__ = 'raw_material'
    id = Column(Integer, ForeignKey('ingredient.id'), primary_key=True)
    price = Column(Float, nullable=True)
    __mapper_args__ = {
        'polymorphic_identity': 'raw_material',
    }

class Recipe(Ingredient):
    __tablename__ = 'recipe'
    id = Column(Integer, ForeignKey('ingredient.id'), primary_key=True)
    ingredients = relationship(
        "Ingredient",
        secondary="ingredient_association",
        backref=backref("recipes"),
        cascade="all, delete"
    )
    __mapper_args__ = {
        'polymorphic_identity': 'recipe',
    }
    def add_ingredient(self, ingredient):
        if isinstance(ingredient, list):
            for unique_ingredient in ingredient:
                self.ingredients.append(unique_ingredient)
        else:
            self.ingredients.append(ingredient)
        self.update_price()

    def remove_ingredient(self, ingredient):
        if isinstance(ingredient, list):
            for unique_ingredient in ingredient:
                self.ingredients.remove(unique_ingredient)
        else:
            self.ingredients.remove(ingredient)
        print(self.price)
        self.update_price()
        print(self.price)

    def update_price(self):
        self.price = sum([ingredient.price for ingredient in self.ingredients])
        

ingredient_association = Table('ingredient_association', db.Model.metadata,
	Column('recipe_id', Integer, ForeignKey('recipe.id')),
	Column('ingredient_id', Integer, ForeignKey('ingredient.id'))
)

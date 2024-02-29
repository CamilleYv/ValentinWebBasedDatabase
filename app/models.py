from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class IngredientAssociation(Base):
    __tablename__ = 'ingredient_association'
    left_id = Column(Integer, ForeignKey('recipe.id'), primary_key=True)
    right_id = Column(Integer, ForeignKey('ingredient.id'), primary_key=True)
    right = relationship("Ingredient")

class Ingredient(Base):
    __tablename__ = 'ingredient' 
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(String(50))
    
    __mapper_args__ = {
        'polymorphic_identity':'ingredient',
        'polymorphic_on':type
    }

class RawMaterial(Ingredient):
    __tablename__ = 'raw_material'
    id = Column(Integer, ForeignKey('ingredient.id'), primary_key=True)
    price = Column(Integer)
    __mapper_args__ = {
        'polymorphic_identity':'raw_material',
    }

class Recipe(Ingredient):
    __tablename__ = 'recipe'
    id = Column(Integer, ForeignKey('ingredient.id'), primary_key=True)
    price = Column(Integer)
    _ingredients = relationship("IngredientAssociation")

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        self._ingredients = value
        self.calculate_price()

    def add_ingredient(self, ingredients):
        if not isinstance(ingredients, list):
            ingredients = [ingredients]
        for ingredient in ingredients:
            self._ingredients.append(ingredient)
        self.calculate_price()

    def remove_ingredient(self, ingredients):
        if not isinstance(ingredients, list):
            ingredients = [ingredients]
        for ingredient in ingredients:
            self._ingredients.remove(ingredient)
        self.calculate_price()

    def calculate_price(self):
        total_price = 0
        for ingredient_association in self.ingredients:
            total_price += ingredient_association.price
        self.price = total_price


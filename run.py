from app import app, db
from app.models import RawMaterial, Recipe

def create_and_test_ingredients():
    # Create raw material instances
    flour = RawMaterial(name='Flour', price=1.1)
    water = RawMaterial(name='Water', price=0.0)

    # Create a recipe instance
    bread = Recipe(name='Bread', price=0.0)

    # Add ingredients to the recipe
    bread.add_ingredient(flour)
    bread.add_ingredient(water)
    db.session.add(bread)
    # Save to database
    db.session.commit()

    # Display the recipe and its ingredients
    print(f"Recipe: {bread.name}, Price: {bread.price}")
    for ingredient in bread.ingredients:
        print(f"Ingredient: {ingredient.name}, Price: {ingredient.price}")

    # Remove an ingredient and show the update
    bread.remove_ingredient(flour)
    db.session.commit()
    print(f"After removing flour, Recipe: {bread.name}, Price: {bread.price}")
    
def setup_database():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    with app.app_context():
        setup_database()
        create_and_test_ingredients()
from flask import Flask, render_template, request, redirect, url_for, jsonify
from extension import db
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///LeValentin.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

app = create_app()
from models import RawMaterial,Recipe,Ingredient

@app.route('/')
def index():
    return render_template('index.html')  # Assume you have an index.html

@app.route('/add_raw_material')
def add_raw_material():
    return render_template('add_raw_material.html')

@app.route('/submit-raw-material', methods=['GET', 'POST'])
def submit_add_raw_material():
    # Handle form submission here if method ipythons POST
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        raw_material = RawMaterial(name=name, price=price)
        db.session.add(raw_material)
        db.session.commit()
        return redirect(url_for('add_raw_material'))

@app.route('/add_recipe')
def add_recipe():
    # Handle form submission here if method is POST
    return render_template('add_recipe.html')

@app.route('/submit-recipe', methods=['GET', 'POST'])
def submit_add_recipe():
    if request.method == 'POST':
        name = request.form['recipeName']
        ingredients = request.form.getlist('ingredient[]')
        quantities = request.form.getlist('quantity[]')
        ingredients_entries = [RawMaterial.query.filter_by(id=ingredient).first() for ingredient in ingredients]
        recipe = Recipe(name=name)
        recipe.add_ingredient(ingredients_entries)
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('add_recipe'))

@app.route('/ingredients')
def get_ingredients():
    ingredients = Ingredient.query.all()  # Assuming Ingredient model exists
    ingredient_list = [{'name': ingredient.name, 'id': ingredient.id} for ingredient in ingredients]
    return jsonify(ingredient_list)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
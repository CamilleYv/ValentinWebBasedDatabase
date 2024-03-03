from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Assume you have an index.html

@app.route('/add_raw_material', methods=['GET', 'POST'])
def add_raw_material():
    # Handle form submission here if method ipythons POST
    return render_template('add_raw_material.html')

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    # Handle form submission here if method is POST
    return render_template('add_recipe.html')

if __name__ == '__main__':
    app.run(debug=True)
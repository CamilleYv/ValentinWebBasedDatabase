from app import app,db,Recipe,RawMaterial

def create_and_test_ingredients():
    # Search for a recipe
    Recipe.query.filter_by(name='Brioche').delete()
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        create_and_test_ingredients()
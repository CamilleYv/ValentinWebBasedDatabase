# Pastry Shop Management Tool

## Project Overview

This web-based application is designed to assist in managing the operations of a pastry shop. It focuses on inventory management, particularly handling raw materials used in pastry production. The current phase of the project involves setting up the foundational elements, including configuring the application structure and defining the raw material model.

## Features

- **Raw Material Management**: Allows for the tracking of raw materials, including their names, prices, and suppliers.

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with Flask-SQLAlchemy for Object-Relational Mapping (ORM)
- **Frontend**: HTML, CSS (with potential use of JavaScript for dynamic content)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- pip
- virtualenv

### Installation

1. **Clone the repository**

   ```
   git clone https://github.com/<your-username>/pastry-shop-management.git
   cd pastry-shop-management
   ```

2. **Set up a virtual environment**

   ```
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Initialize the database**

   ```
   from app import db
   from app import create_app
   
   app = create_app()
   with app.app_context():
       db.create_all()
   ```

### Running the Application

1. **Start the Flask application**

   ```
   flask run
   ```
   
   The application will be accessible at `http://127.0.0.1:5000/`.

## Current Progress

- Configured basic Flask application structure.
- Defined the `RawMaterial` model within the database using Flask-SQLAlchemy, currently tracking:
  - Name
  - Price
  - Supplier

## Contributing

Please read [CONTRIBUTING.md](https://github.com/<your-username>/pastry-shop-management/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/<your-username>/pastry-shop-management/tags).

## Authors

- **Your Name** - *Initial work* - [YourUsername](https://github.com/<your-username>)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc

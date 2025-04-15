from flask import Flask
from flask_migrate import Migrate
from models import db
from routes import app as routes_app

app = routes_app  # Import the app defined in routes.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///late_show.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)

if __name__== '_main_':
    app.run(debug=True)
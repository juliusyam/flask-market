from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '81a8871a4aae6ee2f4300cb8'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from market import routes

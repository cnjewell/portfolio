from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://unit2:unit2pass@localhost:8889/unit2'
app.config['SQLALCHEMY_ECHO'] = True

app.secret_key = 'A0Zr98j/3yXBR~XHH!jmN]LWX/,?RU'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from flask import Flask, request,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import datetime
from flask import Flask, Blueprint
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_persons.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)



from project.books.views import books






app.register_blueprint(books)

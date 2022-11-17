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


from project.core.views  import core
from project.customers.views import customers
from project.books.views import books
from project.loans.views import loans



app.register_blueprint(core)
app.register_blueprint(customers)
app.register_blueprint(books)
app.register_blueprint(loans)

from project import app, db


class Books(db.Model):
    
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    loans= db.relationship('Loans', backref='books')



    def __init__(self,  book_name, author,year,type):
        
        
        self.book_name = book_name
        self.author = author
        self.year = year
        self.type = type
    

with app.app_context():
        db.create_all()
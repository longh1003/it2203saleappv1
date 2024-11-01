from sqlalchemy.orm import relationship
from saleapp.app import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    #Association - Many
    #category - because in mysql table is saved under normalCase
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, default=0)
    image = Column(String(100), nullable=True)
    #Association - One
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
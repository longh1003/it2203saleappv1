from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    cates = dao.load_categories()

    kw = request.args.get('kw')
    cate_id = request.args.get('category_id')
    prods = dao.load_products(kw=kw, category_id=cate_id)
    return render_template('index.html', categories=cates, products=prods)


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)

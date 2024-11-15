from app.models import Category, Product


def load_categories():
    return Category.query.order_by('id').all()


def load_products(kw=None, category_id=None):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    if category_id:
        products = products.filter(Product.category_id == category_id)

    return products.all()

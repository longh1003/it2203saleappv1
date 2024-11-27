from app import db, app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product, User



#tu duy ke thua
class CategoryView(ModelView):
    can_export = True
    column_searchable_list = ['id', 'name']
    column_filters = ['id', 'name']
    can_view_details = True
    column_list = ['name', 'products'] # cot trong models


admin = Admin(app, name='eCommerce', template_mode='bootstrap4')
admin.add_view(CategoryView(Category, db.session))
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(User, db.session))

from django.contrib import admin
from .models import CategoryModel, ProductModel, BranchesModel, CartModel, LikeModel, OrderModel

admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(BranchesModel)
admin.site.register(CartModel)
admin.site.register(LikeModel)
admin.site.register(OrderModel)

from django.urls import path
from .views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("branches/", branches_view, name="branches"),
    path("contacts/", contacts_view, name="contacts"),
    path("auth/", auth_view, name="auth"),
    path("email-code/", email_code_view, name="email_code"),
    path("logout/", logout_view, name="logout"),
    path("add-to-cart/<int:pk>/", add_to_cart_view, name="add_to_cart"),
    path("add-to-cart3/<int:pk>/", add_to_cart3_view, name="add_to_cart3"),
    path("add-like/<int:pk>/", add_like_view, name="add_like"),
    path("add-like2/<int:pk>/", add_like2_view, name="add_like2"),
    path("likes/", likes_view, name="likes"),
    path("cart/", cart_view, name="cart"),
    path("plus_count/<int:pk>/", plus_count_view, name="plus_count"),
    path("minus_count/<int:pk>/", minus_count_view, name="minus_count"),
    path("choose_branch/", choose_branch_view, name="choose_branch"),
    path("choose_branch2/<int:pk>/", branch2_view, name="choose_branch2"),
    path("orders/", orders_view, name="orders"),
    path("product/<int:pk>/", product_view, name="product"),
]
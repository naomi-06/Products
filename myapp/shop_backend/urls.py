from shop_backend import views
from django.urls import path, include
urlpatterns = [
    path('', views.product_list, name='product_list'),
]
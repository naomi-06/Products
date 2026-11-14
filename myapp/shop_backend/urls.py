from shop_backend import views
from django.urls import path, include
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('info/', views.info, name='info')
]
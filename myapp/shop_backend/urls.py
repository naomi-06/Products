from shop_backend import views
from django.urls import path, include
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_details, name='product_details'),
    path('info/', views.info, name='info')
]
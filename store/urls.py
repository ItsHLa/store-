
from django.urls import path
from store import views

urlpatterns = [
    path('products/', views.get_all_products, name='get_products'),
    path('products/<pk>/', views.get_by_id_product, name='get_by_id_product'),
    path('search/', views.get_all_products_by_filter, name='get_all_products_by_filter'),
]

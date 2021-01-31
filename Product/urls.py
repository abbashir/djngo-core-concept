from django.contrib import admin
from django.urls import path
from . import views as product_view

urlpatterns = [
    path('', product_view.product_list, name='product_list'),
    path('<int:id>', product_view.product_details, name='product_details'),
    path('create', product_view.product_create, name='product_create'),
    path('<int:id>/edit', product_view.product_update, name='product_update'),
    path('<int:id>/delete', product_view.product_detete, name='product_delete'),
]

from django.contrib import admin
from django.urls import path
from . import views as blog_view

urlpatterns = [
    path('create', blog_view.blog_create, name='blog_create'),
    path('', blog_view.blog_list, name='blog_list'),
    path('<int:blog_id>', blog_view.blog_details, name='blog_details'),
    path('<int:blog_id>/edit', blog_view.blog_update, name='blog_update'),
    path('<int:blog_id>/delete', blog_view.blog_detete, name='blog_delete'),

    path('form', blog_view.Myform, name='my_form'),
]

from django.urls import path 
from . import views

urlpatterns = [
    path('',views.dashboard),
    path('about/',views.about, name='about'),
    path('support/ ',views.support, name='support'),
    path('product/<int:product_id>/',views.product, name='product'),
    path('categories/', views.categories, name='categories'),
    path('categories/category1', views.category1, name='category1'),
    path('categories/category2', views.category2, name='category2'),
    path('categories/category3', views.category3, name='category3'),
    path('categories/category4', views.category4, name='category4'),

    ]

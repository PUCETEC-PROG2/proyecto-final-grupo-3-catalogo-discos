from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'discos'

urlpatterns = [
    path('', views.index, name='index'),

    # Customer URLs
    path('customer/add/', views.add_customer, name='add_customer'),
    path('customer/edit/<int:id>/', views.edit_customer, name='edit_customer'),
    path('customer/delete/<int:id>/', views.delete_customer, name='delete_customer'),
    path('customer/<int:customer_id>/', views.customer, name='customer'),

    # Category URLs
    path('category/add/', views.add_category, name='add_category'),
    path('category/edit/<int:id>/', views.edit_category, name='edit_category'),
    path('category/delete/<int:id>/', views.delete_category, name='delete_category'),
    path('category/<int:category_id>/', views.category, name='category'),


    # Artist URLs
    path('artist/add/', views.add_artist, name='add_artist'),
    path('artist/edit/<int:id>/', views.edit_artist, name='edit_artist'),
    path('artist/delete/<int:id>/', views.delete_artist, name='delete_artist'),
    path('artist/<int:artist_id>/', views.artist, name='artist'),

    # Product URLs
    path('product/add/', views.add_product, name='add_product'),
    path('product/edit/<int:id>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_product'),
    path('product/<int:product_id>/', views.product, name='product'),

    # Login/Logout URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Purchase URL
    path('purchase/<int:purchase_id>/', views.purchase, name='display_purchase'),
    path('purchase/add/', views.add_purchase, name='add_purchase'),



    path('customers/', views.customer_list, name='customer_list'),
    path('categories/', views.category_list, name='category_list'),
    path('artists/', views.artist_list, name='artist_list'),
    path('products/', views.product_list, name='product_list'),
    path('purchases/', views.purchase_list, name='purchase_list'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),

]

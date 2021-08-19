from django.urls import path, include
# from craigslist_app import views 
from . import views
# from .views import HomeView, CategoryDetailView

urlpatterns = [

    # Category Url
    path('', views.home, name='app-home'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.new_category, name='new_category'),   
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('categories/<int:category_id>/edit/', views.edit_category, name='edit_category'),
    path('categories/<int:category_id>/delete/', views.delete_category, name='delete_category'),


    # Post Url
    path('categories/<int:category_id>/posts', views.post_list, name='post_list'),
    path('categories/<int:category_id>/posts/new/', views.new_post, name='new_post'),
    path('categories/<int:category_id>/posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('categories/<int:category_id>/posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('categories/<int:category_id>/posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),

    
]

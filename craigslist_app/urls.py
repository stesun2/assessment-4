from django.urls import path, include
# from craigslist_app import views 
from . import views
# from .views import HomeView, CategoryDetailView

urlpatterns = [
    # path('', HomeView.as_view(), name='app-home'),
    # path('categories/<int:pk>', CategoryDetailView.as_view(), name='app-categories'),
    



    path('', views.home, name='app-home'),
    path('categories/', views.category_list, name='category_list'),
    # path('categories/new/', views.category_create, name='app-new'),   
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    # path('categories/<int:category_id>/edit/', views.category_edit, name='category-edit'),
    # path('categories/<int:category_id>/delete/', views.category_delete, name='category-delete'),
    # path('categories/<int:category_id>/posts/new/', views.post_create, name='post-create'),
    # path('categories/<int:category_id>/posts/<int:post_id>/', views.post_view, name='post-view'),
    # path('categories/<int:category_id>/posts/<int:post_id>/edit/', views.post_edit, name='post-edit'),
    # path('categories/<int:category_id>/posts/<int:post_id>/delete/', views.post_delete, name='post-delete'),
    # path('', views.index, name='home'),
    # path('<int:category_id>', views.category_detail, name='category_detail'),
    
]

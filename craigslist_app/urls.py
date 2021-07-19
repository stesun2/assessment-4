from django.urls import path, include
from craigslist_app import views 
urlpatterns = [
    path('', views.index, name='home'),
    path('<int:category_id>', views.category_detail, name='category_detail'),
    
]

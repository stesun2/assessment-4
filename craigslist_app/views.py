from django.shortcuts import render
from craigslist_app.models import Category, Post
from .models import *
# from django.views.generic import ListView, DetailView

# class HomeView(ListView):
#     model = Post
#     template_name = 'pages/home.html'

# class CategoryDetailView(DetailView):
#     model = Post
#     template_name = 'pages/category/category_detail.html'

# craigslist_app/templates/pages/base.html
def home(request):
    return render(request, 'pages/home.html')
 
def category_list(request): 
    categories = Category.objects.all()
    return render(request, 'pages/category/category_list.html', {'categories': categories})

def category_detail(request, category_id): 
    category = Category.objects.get(id=category_id)
    return render(request, 'pages/category/category_detail.html', {'category': category})


# def index(request):
#     info = {
#         # referenced in category_list.html
#         "categories": Category.objects.all()
#     }
#     return render(request, "pages/category/category_list.html", info)


# def category_detail(request, category_id):
#     try:
#         category = Category.objects.get(id=category_id)

#     except:
#         return HttpResponse(f"Category with id {category_id} not found!")

#     info = {
#         "category": category
#     }
#     return render(request, "pages/category/category_detail.html", info)


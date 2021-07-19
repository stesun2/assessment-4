from django.http.response import HttpResponse
from django.shortcuts import render
from craigslist_app.models import Category, Post

def index(request):
    info = {
        # referenced in category_list.html
        "categories": Category.objects.all()
    }
    return render(request, "pages/category/category_list.html", info)


# def category_detail(request, category_id):
#     try:
#         category = Category.objects.get(id=category_id)

#     except:
#         return HttpResponse(f"Category with id {category_id} not found!")

#     info = {
#         "category": category
#     }
#     return render(request, "pages/category/category_detail.html", info)


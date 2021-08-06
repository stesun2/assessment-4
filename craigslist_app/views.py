from django.shortcuts import render
from craigslist_app.models import Category, Post

# Dummy inputs
posts = [
    {
        'author': 'Joe',
        'title': 'Used Cars',
        'content': 'Used Cars for sale',
        'date_posted': '8/6/21'
    },
    {
        'author': 'Jane',
        'title': 'computer parts',
        'content': 'Selling used hardware',
        'date_posted': '8/6/21'
    }
]

# craigslist_app/templates/pages/base.html
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'pages/home.html', context)

def category(request):
    return render(request, 'pages/category/category_detail.html')

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


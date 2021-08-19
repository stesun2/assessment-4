from django.shortcuts import redirect, render
from .models import Category
from .forms import CategoryForm
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

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm()
        return render(request, 'pages/category/category_form.html', {'form': form, 'type_of_request': 'New'})

def edit_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
        return render(request, 'pages/category/category_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_category(request, category_id):
    if request.method == "POST":
        category = Category.objects.get(id=category_id)
        category.delete()
    return redirect('category_list')



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

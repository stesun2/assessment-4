from django.shortcuts import redirect, render
from .models import Category, Post
from .forms import CategoryForm, PostForm
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

########## POST ##################
def post_list(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = category.posts.all()
    return render(request, 'pages/post/post_list.html', {'category': category, 'posts': posts})

def post_detail(request, category_id, post_id):
    category = Category.objects.get(id=category_id)
    post = Post.objects.get(id=post_id) 
    return render(request, 'pages/post/post_detail.html', {'category': category, 'post': post})

def new_post(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = category
            post.save()
            return redirect('post_detail', category_id=category.id, post_id=post.id)
    else:
        form = PostForm({'category': category})
        return render(request, 'pages/post/post_form.html', {'form': form, 'type_of_request': 'New'})

def edit_post(request, category_id, post_id):
    category = Category.objects.get(id=category_id)
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', post_id=post.id, category_id=category.id)
    else:
        form = PostForm(instance=post)
        return render(request, 'pages/post/post_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_post(request, category_id, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.delete()
    return redirect('post_list', category_id=category.id)


# def new_category(request):
#     if request.method == "POST":
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             category = form.save(commit=False)
#             category.save()
#             return redirect('category_detail', category_id=category.id)
#     else:
#         form = CategoryForm()
#         return render(request, 'pages/category/category_form.html', {'form': form, 'type_of_request': 'New'})

# def edit_category(request, category_id):
#     category = Category.objects.get(id=category_id)
#     if request.method == "POST":
#         form = CategoryForm(request.POST, instance=category)
#         if form.is_valid():
#             category = form.save(commit=False)
#             category.save()
#             return redirect('category_detail', category_id=category.id)
#     else:
#         form = CategoryForm(instance=category)
#         return render(request, 'pages/category/category_form.html', {'form': form, 'type_of_request': 'Edit'})

# def delete_category(request, category_id):
#     if request.method == "POST":
#         category = Category.objects.get(id=category_id)
#         category.delete()
#     return redirect('category_list')


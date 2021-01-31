from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.db.models import Q
from .models import PostModel
from .form import postCreateForm, MyForm


def blog_create(request):
    create_form = postCreateForm(request.POST or None)
    if request.method == 'POST':
        if create_form.is_valid():
            obj = create_form.save(commit=False)
            obj.save()
            messages.success(request, 'Post Created.')
            # return HttpResponseRedirect("/blog/{id}".format(id=obj.id))
            return redirect('blog_list')

    context = {
        "title": "Create blog",
        "form": create_form
    }
    return render(request, "blog/blog_create.html", context)


# Create your views here.
# @login_required
def blog_list(request):
    # print("OK")
    # print(request.get_full_path())
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # print(request.user)
    # if request.user.is_authenticated:
    #     print("Logged")
    # else:
    #     print("Not login")
    query = request.GET.get('q', None)
    blogs = PostModel.objects.all()

    if query is not None:
        blogs = blogs.filter(
            Q(title__contains=query) |
            Q(content__contains=query)
        )

    context = {
        'blogs': blogs
    }
    return render(request, "blog/blog_list.html", context)


def blog_details(request, blog_id):
    blog = get_object_or_404(PostModel, pk=blog_id)
    print(blog_id)
    context = {
        "blog": blog
    }
    return render(request, "blog/blog_details.html", context)


def blog_update(request, blog_id):
    obj = get_object_or_404(PostModel, pk=blog_id)
    form = postCreateForm(request.POST or None, instance=obj)

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'Post Updated.')
            return redirect('blog_list')

    context = {
        "title": "Update blog",
        "form": form
    }
    return render(request, "blog/blog_update.html", context)


def blog_detete(request, blog_id):
    blog = get_object_or_404(PostModel, pk=blog_id)
    if request.method == 'GET':
        blog.delete()
        messages.success(request, 'Post Deleted.')
    context = {
        "blog": blog
    }
    return redirect('blog_list')


def Myform(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('name'))
            print(form.cleaned_data)
    else:
        form = MyForm()
    context = {
        'form': form
    }
    return render(request, 'blog/myForm.html', context)

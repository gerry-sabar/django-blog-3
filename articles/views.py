from django.shortcuts import render  # this will be used to use template page
# we need this to check whether or not the article exists
from django.shortcuts import get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm  # importing form to be rendered at template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404


def index(request):
    query = Article.objects.all()  # get all records from article
    page = request.GET.get('page')
    paginator = Paginator(query, 3)  # display 3 articles per page

    try:
        articles = paginator.page(page)  # display article according to url parameter page
    except PageNotAnInteger:
        articles = paginator.page(1)  # if parameter page is not integer set to display page 1
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)  # if page doesn't exist, use last page

    data = {
        "articles": articles,
    }
    return render(request, "index.html", data)  # render articles into template index.html


def detail(request, id):  # we get id parameter from articles/urls.py
    article = get_object_or_404(Article, id=id)  # this equal to search article where id is equal to parameter
    data = {
        "article": article,
    }
    return render(request, "detail.html", data)


def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = ArticleForm(request.POST, request.FILES)  # form will hold input forms those are defined in articles/forms.py
    if form.is_valid():   # if the request is POST, form will hold submitted value then save into database
        article = form.save(commit=False)
        article.save()
        form = ArticleForm()  # removing previously input data in form
    data = {
        "form": form,
    }
    return render(request, "create.html", data)

def update(request, id):  # basically identical with detail to get the parameter
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, instance=article)  # load article data to form
    if form.is_valid():
        article = form.save(commit=False)
        article.save()
    data = {
        "article": article,
        "form": form,
    }
    return render(request, "create.html", data)  # we can use the same form to create article

def delete(request, id=None):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect("index")  # redirect to index page after remove article



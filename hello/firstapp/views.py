from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


# Create your views here.
def index(request):
    return render(request, "firstapp/index.html")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


# Listing 4.6
def products(request, product_id):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1}</h2>".format(product_id, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Вася")
    output = "<h2>Пользователь</h2><h3> id: {0} Имя: {1}</h3>".format(id, name)
    return HttpResponse(output)

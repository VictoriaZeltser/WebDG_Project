from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Добро пожаловать на нашу первую страницу</h1>')

def data(request):
    return HttpResponse("<h1>Приветствую вас на второй странице.</h1>")

def test(request):
    return HttpResponse("<h1>И снова здравствуйте на третьей странице.</h1>")

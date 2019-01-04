from django.http import HttpResopnse
from django.shortcuts import redirect

def index(request):
    return HttpResopnse('index')

def login(request):
    return redirect('/index')

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def new(request):
    pass

def create(request):
    pass

def show(request, user_id):
    pass

def edit(request, user_id):
    pass

def update(request, user_id):
    pass

def delete(request, user_id):
    pass
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


#can only use session and messages from views - so anything related to that - we have to send it back to the views.

# Create your views here.
def index(request):
#    return render(request, 'main/index.html')
    context = {
        'users': User.objects.all()
    }
    return render(request, 'main/index.html', context)

def new(request):
    return render(request, 'main/new.html')

def create(request):
    if request.method != 'POST':
        return redirect('/main/new')
    valid, response = User.objects.validate(request.POST) 
    #request.POST is the form_data (a dictionary) that we're passing in from the validate method on the UserManager model in models.py 
    #'valid, response' will be used for tuple unpacking. if there are exactly the same number of items returned as in the variable, we can group them in the same line. These will correspond to 'True/False, errors' from models.py
    if valid:
        request.session['user_id'] = response.id
        #response is second thing in tuple, cooresponds to 'user' in models.py return statement after except.
    else:
        for error in response:
            messages.error(request, error)
    return redirect('/main/new')

def show(request):
    '''
    try:
        user = User.objects.get(id=user_id)
    except:
        return redirect('/main')
    context = {
        'user': user
    }
    '''
    return render(request, 'main/show.html')

def edit(request, user_id):
    pass

def update(request, user_id):
    pass

def delete(request, user_id):
    pass

def login(request):
    if request.method != 'POST':
        return redirect('/main/new')

    valid, response = User.objects.validatelogin(request.POST)
    #print request.POST
    if valid == False:
        for error in response:
            messages.error(request, error)
        return redirect('/main/new')
    else:
        request.session['user_id'] = response.id
        return redirect('/main/show')

    
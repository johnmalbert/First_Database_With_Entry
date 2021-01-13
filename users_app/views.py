from django.shortcuts import render, HttpResponse, redirect
from .models import User
# Create your views here.
def index(request):
    context = {
        "all_users" : User.objects.all()
    }
    return render(request, "index.html", context)

def create_user(request):
    #get user input ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)
    request.session['error'] = False
    try:
        first = (request.POST['first_name'])
        last = (request.POST['last_name'])
        email = (request.POST['email'])
        age = int(request.POST['age'])
        User.objects.create(first_name=first, last_name=last, email_address=email, age=age)
    except:
        print("missing data")
        request.session['error'] = True
    return redirect('/')

def reset(request):
    return HttpResponse("placeholder to later reset database")
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import *

# Create your views here.
def login(request):
    if request.method =='POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = Teacher.objects.filter(username = username).first()
        if not user:
            return render(request,{'message' : 'Invalid Username!!'})
        
        if check_password(password, user.password):
            request.session['teacher_id'] = user.id
            request.session['teacher_username'] = user.username
            return redirect("/dashboard")
        else:
            return render(request,{'message' : 'Invalid Password!!'})
    else:
        return render(request, 'tech/login.html')
    

def register(request):
    print(request.method)
    if request.method == 'POST':
        data = request.POST
        print(data.get('username'))
        try:
            user = Teacher.objects.filter(username=data.get('username')).first()
            print(user)
            if user:
                return render(request, 'register.html', {
                    'message': 'User already registered'
                })
            print("Password : ",data.get('password'))
            Teacher.objects.create(
                name=data.get('name'),
                number=int(data.get('number')),
                email=data.get('email'),
                username=data.get('username'),
                password=make_password(data.get('password'))
            )
            # print(Teacher)
            return redirect("/login")

        except ValueError:
            return render(request, 'tech/register.html', {
                'message': 'Invalid phone number'
            })

        except Exception as e:
            print(e)

            return render(request, 'tech/register.html', {
                'message': str(e)
            })

    return render(request, 'tech/register.html')
    


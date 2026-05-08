from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def login(request):
    if request.method =='POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = Teacher.objects.filter(username = username).first()
        if not user:
            return {'message' : 'Invalid Username!!'}
        
        if user.password == password:
            return redirect("/dashboard")
        else:
            return {'message' : 'Invalid Password!!'}
    else:
        return render(request, 'tech/login.html')
    

def register(request):
    if request.method == 'POST':
        data = request.POST

        try:
            user = Teacher.objects.filter(
                username=data.get('username')
            ).first()

            if user:
                return render(request, 'register.html', {
                    'message': 'User already registered'
                })

            Teacher.objects.create(
                name=data.get('name'),
                number=int(data.get('number')),
                email=data.get('email'),
                username=data.get('username'),
                password=data.get('password')
            )

            return redirect("/login")

        except ValueError:
            return render(request, 'register.html', {
                'message': 'Invalid phone number'
            })

        except Exception as e:
            return render(request, 'register.html', {
                'message': f'Error: {str(e)}'
            })

    return render(request, 'tech/register.html')
    


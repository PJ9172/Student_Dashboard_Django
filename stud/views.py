from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def get_students(request):
    if request.method == 'GET':
        student = Students.objects.all()
        if student:
            context = {
                'students' : student
            }
            return render(request, 'stud/dashboard.html', context)
        else:
            return render(request, "stud/dashboard.html", context={'message' : 'Students not available!!!'})
    
    elif request.method == 'POST':
        data = request.POST
        try:
            Students.objects.create(
                name = data.get('name'),
                number = data.get('number'),
                email = data.get('email'),
                percentage = data.get('percentage')
            )
            return redirect("/dashboard")
        except Exception as e:
            return {'error' : e}
    else:
        return {'message' : 'Invalid method!!!'}
    

def update(request):
    id = request.GET.get('id')
    student = Students.objects.filter(id=id).first()
    if request.method == 'POST':
        if student:
            data = request.POST
            name = data.get('name')
            number = data.get('number')
            email = data.get('email')
            percentage = data.get('percentage')

            Students.objects.filter(id=id).update(
                name=name, number=number, email=email, percentage=percentage
            )
            
            return redirect('/dashboard')
        else:
            return render(request, 'stud/update.html',context = {'message' : 'Invalid Student ID'})
    
    elif request.method == 'GET':
        context = {
            'student' : student
        }
        return render(request, 'stud/update.html', context)
    

def delete(request):
        id = request.GET.get('id')
        Students.objects.filter(id=id).delete()
        return redirect("/dashboard")

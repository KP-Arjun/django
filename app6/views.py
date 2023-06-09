from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from.models import Departments,Doctors
from .forms import BookingForm


# Create your views here.

def index(req):
    numbers={
        'num1':[1,2,3,4,5]
    }
    return render(req,'index.html',numbers)
def about(req):
    return render(req,'aboutpage.html')



def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form={
       'form': form
    }
    return render(request, "bookings.html",dict_form)
    

def doctors(req):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(req, 'doctors.html', dict_docs)
def contact(req):
    return render(req,'contact.html')
def department(req):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(req,'Departments.html',dict_dept)
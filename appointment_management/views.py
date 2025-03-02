from django.shortcuts import render,redirect
from . models import Business_History,BookAppointment
from datetime import timedelta,datetime
from user_management.models import user_profile



def create_business_history(request):
    if request.method == "POST":
        status = request.POST['status']
        business_data = Business_History.objects.create(business_man_id=request.user.id,start_datetime=datetime.now(),status=status)
        business_data.save()
        return redirect('customer_list')


def book_appointment(request,id):
    if request.method == "POST":
        datetime = request.POST['datetime']
        book_appointment = BookAppointment.objects.create(business_man_id=id,customer_id=request.user.id,datetime=datetime)
        book_appointment.save()
        return redirect('business_man_list')
    else:
        user_data = user_profile.objects.filter(id=id).first()
        return render(request,'book-appointment.html',{'data':user_data})


def clients_appointment_list(request):
    client_data = BookAppointment.objects.filter(customer_id=request.user.id)
    return render(request,'appointment-list.html',{'data':client_data})

def business_appointment_list(request):
    business_man_data = BookAppointment.objects.filter(business_man_id=request.user.id)
    return render(request, 'appointment-list.html', {'data': business_man_data})

def appointment_list(request):
    data = BookAppointment.objects.all()
    return render(request,'appointment-list.html',{'data':data})

def terms(request):
    return render(request,'terms.html')

def business_man_terms(request):
    return render(request,'business-man-terms.html')
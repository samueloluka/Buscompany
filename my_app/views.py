from django.shortcuts import render, redirect

from my_app.forms import BusForm, DriverForm, TripForm, BookingForm, PaymentForm
from my_app.models import Bus, Driver, Trip, Booking, Payment
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

@login_required
def index_view(request):
        return render(request, 'index.html')
@login_required
def bus_view(request):
        return render(request, 'bus.html')

def driver_view(request):
        return render(request, 'driver.html')

def trip_view(request):
        return render(request, 'trip.html')

def booking_view(request):
        return render(request, 'booking.html')

def payment_view(request):
        return render(request, 'booking.html')
@login_required
def add_bus_view(request):
        message= ''
        if request.method == "POST":
                bus_form = BusForm(request.POST)

                if bus_form.is_valid():
                        bus_form.save()

                        messages.success(request, "Bus Added Successfully")

        
        bus_form = BusForm()
        buss = Bus.objects.all()

        context = {

                'form':bus_form,
                'msg':message,
                'buss':buss
                

        }
        return render(request, "add_bus.html", context)
@login_required
def add_driver_view(request):
        message=''
        if request.method == "POST":
                driver_form = DriverForm(request.POST, request.FILES)

                if driver_form.is_valid():
                        driver_form.save()

                        messages.success(request, "Driver Added Successfully")

        
        driver_form = DriverForm()

        drivers = Driver.objects.all()

        context = {

                'form':driver_form,
                'msg':message,
                'drivers':drivers
        }
        return render(request, "add_driver.html", context)
@login_required
def add_trip_view(request):
        message= ''
        if request.method == "POST":
                trip_form = TripForm(request.POST)

                if trip_form.is_valid():
                        trip_form.save()

                        messages.success(request, "Trip Added Successfully")

        
        trip_form = TripForm()
        trips = Trip.objects.all()

        context = {

                'form':trip_form,
                'msg':message,
                'trips':trips
                

        }
        return render(request, "add_trip.html", context)
@login_required
def add_booking_view(request):
        message=''
        if request.method == "POST":
                booking_form = BookingForm(request.POST)

                if booking_form.is_valid():
                        booking_form.save()

                        messages.success(request, "Booking Added Successfully")

        
        booking_form = BookingForm()

        bookings = Booking.objects.all()

        context = {

                'form':booking_form,
                'msg':message,
                'bookings':bookings
        }
        return render(request, "add_booking.html", context)
@login_required
def add_payment_view(request):
        message=''
        if request.method == "POST":
                payment_form = PaymentForm(request.POST)

                if payment_form.is_valid():
                        payment_form.save()

                        messages.success(request, "Payment Added Successfully")

        
        payment_form = PaymentForm()

        payments = Payment.objects.all()

        context = {

                'form':payment_form,
                'msg':message,
                'payments':payments
        }
        return render(request, "add_payment.html", context)


@login_required
def edit_bus_view(request, bus_id):
        message=''
        bus = Bus.objects.get(id=bus_id)

        if request.method =="POST":
                bus_form = BusForm( request.POST,instance=bus)

                if bus_form.is_valid():
                        bus_form.save()
                        messages.success(request, "Bus Edited Successfully")
                        return redirect(add_bus_view)

                else:
                        message= "Form has invalid data"

        else:
                bus_form = BusForm( instance = bus)

        context ={
                'form':bus_form,
                'bus':bus,
                'message':message
                
        }

        return render(request, 'edit_bus.html', context)
        
@login_required
def edit_driver_view(request, driver_id):
        message=''
        driver = Driver.objects.get(id=driver_id)

        if request.method =="POST":
                driver_form = DriverForm(request.POST, request.FILES, instance=driver)

                if driver_form.is_valid():
                        driver_form.save()
                        messages.success(request, "Driver Edited Successfully")
                        return redirect(add_driver_view)

                else:
                        message= "Form has invalid data"

        else:
                driver_form = DriverForm( instance = driver)

        context ={
                'form':driver_form,
                'driver':driver,
                'message':message
        }

        return render(request, 'edit_driver.html', context)

@login_required
def edit_trip_view(request, trip_id):
        message = ''
        trip = Trip.objects.get(id=trip_id)

        if request.method =="POST":
                trip_form = TripForm(request.POST, instance=trip)

                if trip_form.is_valid():
                        trip_form.save()
                        messages.success(request, "Trip Edited Successfully")
                        return redirect(add_trip_view)

                else:
                        message= "Form has invalid data"

        else:
                trip_form = TripForm( instance = trip)

        context ={
                'form':trip_form,
                'trip':trip,
                'message':message
        }

        return render(request, 'edit_trip.html', context)
@login_required        
def edit_booking_view(request, booking_id):
        message=''
        booking = Booking.objects.get(id=booking_id)

        if request.method =="POST":
                booking_form = BookingForm(request.POST, instance=booking)

                if booking_form.is_valid():
                        booking_form.save()
                        messages.success(request, "Booking Edited Successfully")
                        return redirect(add_booking_view)

                else:
                        message= "Form has invalid data"

        else:
                booking_form = BookingForm( instance = booking)

        context ={
                'form':booking_form,
                'booking':booking,
                'message':message
        }

        return render(request, 'edit_booking.html', context)
@login_required        
def edit_payment_view(request, payment_id):
        message=''
        payment = Payment.objects.get(id=payment_id)

        if request.method =="POST":
                payment_form = PaymentForm(request.POST, instance=payment)

                if payment_form.is_valid():
                        payment_form.save()
                        messages.success(request, "Payment Edited Successfully")
                        return redirect(add_payment_view)

                else:
                        message= "Form has invalid data"

        else:
                payment_form = PaymentForm( instance = payment)

        context ={
                'form':payment_form,
                'payment':payment,
                'message':message
        }

        return render(request, 'edit_payment.html', context)
        
@login_required
def delete_bus_view(request, bus_id):
        bus = Bus.objects.get(id=bus_id)

        bus.delete()

        return redirect(add_bus_view)
@login_required
def delete_driver_view(request, driver_id):
        driver = Driver.objects.get(id=driver_id)

        driver.delete()

        return redirect(add_driver_view)
@login_required
def delete_trip_view(request, trip_id):
        trip = Trip.objects.get(id=trip_id)

        trip.delete()

        return redirect(add_trip_view)
@login_required
def delete_booking_view(request, booking_id):
        booking = Booking.objects.get(id=booking_id)

        booking.delete()

        return redirect(add_booking_view)
@login_required
def delete_payment_view(request, payment_id):
        payment = Payment.objects.get(id=payment_id)

        payment.delete()

        return redirect(add_payment_view)

def sign_up_view(request):
        if request.method=="POST":
                sign_up_form = UserCreationForm(request.POST)      
                if sign_up_form.is_valid():
                        sign_up_form.save()

                        message= 'User created successfully'

                else:
                        message='Someting went wrong'      

        else:
                sign_up_form= UserCreationForm()
        context={
                'form':sign_up_form
        }
        return render(request, 'registration/sign_up.html', context )


        






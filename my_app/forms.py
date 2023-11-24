from django.forms import ModelForm

from my_app.models import Bus, Driver, Trip, Booking, Payment


class BusForm(ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'

class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

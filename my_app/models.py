from django.db import models

class Bus(models.Model):
    plate_no = models.CharField(max_length = 40)
    model = models.CharField(max_length =30)
    brand = models.CharField(max_length = 30)
    capacity = models.IntegerField()
    

    def __str__(self):
        return f"{self.plate_no}-{self.model}-{self.brand}-{self.capacity}"

class Driver(models.Model):
    driver_name = models.CharField(max_length = 28)
    address = models.CharField(max_length = 26)
    contact = models.CharField(max_length = 14)
    bus = models.ForeignKey(Bus, on_delete = models.CASCADE)
    photo = models.ImageField(upload_to="photos/")

    def __str__(self):
        return f"{self.bus}"





class Trip(models.Model):
    trip_date = models.DateField(auto_now = False)
    
    departure_time = models.DateTimeField(auto_now=False)
    departure_place = models.CharField(max_length = 22)
    destination = models.CharField(max_length = 22)
    bus = models.ForeignKey(Bus, on_delete = models.CASCADE)
    amount = amount = models.DecimalField(default=True, max_digits=10, decimal_places=2)

    

    def __str__(self):
        return f"{self.trip_date}-{self.departure_time}-{self.departure_place}-{self.destination}-{self.bus}-{self.amount}"


class Booking(models.Model):
    customer_name = models.CharField(max_length = 27)
    contact = models.CharField(max_length = 15)
    seat_no = models.IntegerField()
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.customer_name}-{self.contact}-{self.seat_no}-{self.trip}"


class Payment(models.Model):
    Payment_date = models.DateField(auto_now = False)
    booking = models.ForeignKey(Booking, on_delete = models.CASCADE)
    amount_paid = models.IntegerField()
    received_by = models.CharField(max_length = 26)

    def __str__(self):
        return f"{self.Payment_date}-{self.booking}-{self.amount_paid}-{self.received_by}"


from django.contrib import admin

from .models import Bus, Driver, Trip, Booking, Payment

class BusAdmin(admin.ModelAdmin):
    list_display = ("plate_no", "model", "brand", "capacity")





class DriverAdmin(admin.ModelAdmin):
    list_display = ("driver_name", "address", "contact", "bus")

class TripAdmin(admin.ModelAdmin):
    list_display = ("trip_date", "departure_time", "departure_place", "destination", "bus")

class BookingAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "contact", "seat_no", "trip")

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("Payment_date", "amount_paid", "received_by", "booking")








admin.site.register(Bus, BusAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment, PaymentAdmin)

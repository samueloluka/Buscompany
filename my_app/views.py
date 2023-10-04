from django.shortcuts import render

def index_view(request):
        return render(request, 'index.html')

def bus_view(request):
        return render(request, 'bus.html')

def driver_view(request):
        return render(request, 'driver.html')

def trip_view(request):
        return render(request, 'trip.html')

"""
URL configuration for buscompany project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from my_app.views import index_view, bus_view, driver_view, payment_view,booking_view, trip_view, add_bus_view, add_driver_view, add_trip_view, add_booking_view, add_payment_view, edit_bus_view, edit_driver_view, edit_trip_view, edit_booking_view, edit_payment_view, delete_bus_view, delete_driver_view, delete_trip_view, delete_booking_view, delete_payment_view, sign_up_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index_page'),
    path('sign_up/', sign_up_view, name='sign_up_page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('bus_details', bus_view, name='bus_page'),
    path('booking_details', booking_view, name='booking_page'),
    path('payment_details', payment_view, name='payment_page'),
    path('driver_details', driver_view, name='driver_page'),
    path('trip_details', trip_view, name='trip_page'),
    path('add_bus', add_bus_view, name="add_bus_page"),
    path('add_driver', add_driver_view, name="add_driver_page"),
    path('add_trip', add_trip_view, name="add_trip_page"),
    path('add_booking', add_booking_view, name="add_booking_page"),
    path('add_payment', add_payment_view, name="add_payment_page"),
    path('edit_bus/<int:bus_id>/', edit_bus_view, name="edit_bus_page"),
    path('edit_driver/<int:driver_id>/', edit_driver_view, name="edit_driver_page"),
    path('edit_trip/<int:trip_id>/', edit_trip_view, name="edit_trip_page"),
    path('edit_booking/<int:booking_id>/', edit_booking_view, name="edit_booking_page"),
    path('edit_payment/<int:payment_id>/', edit_payment_view, name="edit_payment_page"),
    path('delete_bus/<int:bus_id>/', delete_bus_view, name="delete_bus_page"),
    path('delete_driver/<int:driver_id>/', delete_driver_view, name="delete_driver_page"),
    path('delete_trip/<int:trip_id>/', delete_trip_view, name="delete_trip_page"),
    path('delete_booking/<int:booking_id>/', delete_booking_view, name="delete_booking_page"),
    path('delete_payment/<int:payment_id>/', delete_payment_view, name="delete_payment_page")



]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

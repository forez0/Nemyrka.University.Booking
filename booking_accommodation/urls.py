# urls.py in your app directory

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'accommodations', views.AccommodationViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    path('', include('router.urls')),
]

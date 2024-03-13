"""
URL configuration for CityVotingPlatform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from city_voting_registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("allauth.urls")),
    path('accounts/google/login/callback/', views.callback_view, name='google_callback'),
    path('', include('city_voting_registration.urls')),
    path('', include('city_map.urls')),
    path('', views.home, name='home'),
]

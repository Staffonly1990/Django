from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('profile/', include('Profile.urls')),
]
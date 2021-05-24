from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
	path('', Profile.as_view(), name='profile'),
	path('my_orders/', MyOrders.as_view(),name='my_orders'),
	path('data_correction/', DataCorrection.as_view(), name='data_correction'),
	path('logout/', logout_user, name='logout_user'),
	path('add_order/', AddOrder.as_view(), name='add_order'),
]
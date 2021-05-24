from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView

from Orders.models import Orders, OrderStaff
from Profile.forms import *
from Users.models import Users

class AddOrder(LoginRequiredMixin,CreateView):
	form_class = AddOrderForm
	login_url = reverse_lazy('login')
	template_name = 'Profile/add_order.html'
	context_object_name = 'user'
	success_url = reverse_lazy('my_orders')
	
	
	def get_queryset(self):
		return self.request.user
	
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(AddOrder, self).get_context_data(**kwargs)
		return context
	
	def form_valid(self, form):
		order = form.save(commit=False)
		order.save()
		OrderStaff.objects.create(orders=order,users=self.request.user)
		return redirect('my_orders')
	


class Profile(LoginRequiredMixin, ListView):
	template_name = 'Profile/profile.html'
	# model = Users
	context_object_name = 'user'
	login_url = reverse_lazy('login')
	
	def get_queryset(self):
		return self.request.user
	
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(Profile, self).get_context_data(**kwargs)
		return context


class MyOrders(LoginRequiredMixin,ListView):
	# model = Orders
	template_name = 'Profile/my_orders.html'
	context_object_name = 'user'
	login_url = reverse_lazy('login')
	
	
	def get_queryset(self):
		return self.request.user
	
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(MyOrders, self).get_context_data(**kwargs)
		context['orders'] = Orders.objects.filter(orderstaff__users_id=self.request.user.id)
		return context
	
class DataCorrection(LoginRequiredMixin,View):
	template_name = 'Profile/data_correction.html'
	login_url = reverse_lazy('login')
	
	def post(self, request):
		if request.method == 'POST':
			settings_form = DataCorrectionForm(request.POST, instance=self.request.user)
			if settings_form.is_valid():
				settings_form.save()
			return render(request, self.template_name, {'form': settings_form,'user':self.request.user})
	
	def get(self, request):
		settings_form = DataCorrectionForm(instance=self.request.user)
		return render(request, self.template_name, {'form': settings_form,'user':self.request.user})
	
def logout_user(request):
	logout(request)
	return redirect('login')
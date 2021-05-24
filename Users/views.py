from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from Users.forms import *
from WillDoc import settings

		


class Register(CreateView):
	form_class = RegisterUserForm
	template_name = 'Users/register.html'
	
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(settings.LOGIN_REDIRECT_URL)
		else:
			return super().dispatch(request, *args, **kwargs)
	
	def form_valid(self, form):
		user = form.save(commit=False)
		user.save()
		group = Group.objects.get(name=form.cleaned_data['groups'])
		user.groups.add(group)
		return redirect('login')
	
	def get_context_data(self, **kwargs):
		context = super(Register, self).get_context_data(**kwargs)
		return context
	
class LoginUser(LoginView):
	form_class = LoginUserForm
	template_name = 'Users/login.html'
	
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect(settings.LOGIN_REDIRECT_URL)
		else:
			return super().dispatch(request, *args, **kwargs)
	
	def get_success_url(self):
		return reverse_lazy('profile')
	
	def get_context_data(self,**kwargs):
		context = super(LoginUser,self).get_context_data(**kwargs)
		return context
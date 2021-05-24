from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import Group
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import get_language, ugettext_lazy as _

from Users.models import Users

class LoginUserForm(AuthenticationForm):
	username = UsernameField(
		label='',
		widget=forms.TextInput(attrs={'autofocus': True,'class': 'login_class','placeholder':'Введите ваш e-mail'})
	)
	password = forms.CharField(
		label='',
		strip=False,
		widget=forms.PasswordInput(attrs={'class': 'password_class','placeholder':'Введите ваш пароль'}),
	)
	remember = forms.BooleanField(
		label='Запомнить меня',
		widget=forms.CheckboxInput(attrs={'class':'maybe_class'})
	)

class RegisterUserForm(UserCreationForm):
	username = forms.CharField(
		label='',
		widget=forms.TextInput(attrs={'placeholder':'Ваше имя','class':'my_class_us'})
	)
	password1 = forms.CharField(
		label='',
		widget=forms.PasswordInput(attrs={'placeholder':'Придумайте пароль','class':'my_class_us'})
	)
	password2 = forms.CharField(
		label='',
		widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль', 'class': 'my_class_us'})
	)
	email = forms.EmailField(
		label='',
		widget=forms.EmailInput(attrs={'placeholder': 'Ваш e-mail', 'class': 'my_class_us'})
	)
	phone = PhoneNumberField(
		label="",
		widget=forms.TextInput(attrs={'placeholder':'Ваш номер телефона','class':'my_class_us'}),
		error_messages = {'invalid':'Просим ввести телефон в формате +71111111111', 'already':'Такой ноер уже существует'}
	)
	groups = forms.ModelChoiceField(
		label='',
		queryset=Group.objects.all()
	)
	consent = forms.BooleanField(
		label='Я согласен на обработку персональных данных',
		widget=forms.CheckboxInput(attrs={'class':'my_class_us'}),
	)
	
	def clean_phone(self):
		phone = self.cleaned_data['phone']
		users = Users.objects.filter(phone=phone)
		if users:
			raise forms.ValidationError("Номер уже занят")
		return phone
	
	def clean_consent(self):
		consent = self.cleaned_data['consent']
		if not consent:
			raise forms.ValidationError("Поставь галочку")
		return consent
		
	def __init__(self,*args,**kwargs):
		super(RegisterUserForm, self).__init__(*args,**kwargs)
		self.fields['groups'].empty_label='Вы'
		
	class Meta:
		model=Users
		fields = ['username','password1','password2','email','phone','groups','consent']
		
		
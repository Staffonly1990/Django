from django import forms

from Orders.models import Orders
from Users.models import Users
from phonenumber_field.formfields import PhoneNumberField

class AddOrderForm(forms.ModelForm):
	class Meta:
		model = Orders
		fields = ['title','content','pricer','photo','categories']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['categories'].empty_label = 'Не выбрано'
		

class DataCorrectionForm(forms.ModelForm):
	username = forms.CharField(
		label='',
		widget=forms.TextInput(attrs={'placeholder': 'Ваше имя', 'class': 'my_class_us'})
	)
	dop_info = forms.CharField (
		label='',
		widget=forms.TextInput(attrs={'placeholder': 'Дополнительная информация', 'class': 'my_class_us'})
	)
	phone = PhoneNumberField(
		label="",
		widget=forms.TextInput(attrs={'placeholder': 'Ваш номер телефона', 'class': 'my_class_us'}),
		error_messages={'invalid': 'Просим ввести телефон в формате +71111111111',
		                'already': 'Такой ноер уже существует'})
	email = forms.EmailField(
		label='',
		widget=forms.EmailInput(attrs={'placeholder': 'Ваш e-mail', 'class': 'my_class_us'})
	)
	
	
	def clean_phone(self):
		phone = self.cleaned_data['phone']
		users = Users.objects.filter(phone=phone)
		if users:
			if self.instance.slug_user == users[0].slug_user:
				return phone
			else:
				raise forms.ValidationError("Номер уже занят")
		return phone
	
	def clean_email(self):
		email = self.cleaned_data['email']
		users = Users.objects.filter(email=email)
		if users:
			if self.instance.slug_user == users[0].slug_user:
				return email
			else:
				raise forms.ValidationError("email уже занят")
		return email
	
	class Meta:
		model = Users
		fields = ['username','email','dop_info','phone','photo']
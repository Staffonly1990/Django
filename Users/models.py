from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import get_language, ugettext_lazy as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from pytils.translit import slugify

class Users(AbstractUser):
	username = models.CharField(verbose_name='Имя пользователя',max_length=150,unique=False,blank=False)
	dop_info = models.TextField(verbose_name='Дополнительная информация',blank=True)
	wallet = models.IntegerField(verbose_name='Кошелек',default=0)
	phone = PhoneNumberField(verbose_name='Телефон',null=False, blank=False, unique=True)
	photo = models.ImageField(verbose_name='Фото', upload_to='photo/users/%Y/%m/%d',blank=True,default='default.png')
	email = models.EmailField(verbose_name='e-mail',blank=False,unique=True)
	rating = models.IntegerField(verbose_name='Рейтинг', default=0)
	confirm = models.BooleanField(verbose_name='Подтвержден', default=0)
	consent = models.BooleanField(verbose_name='Согласие', default=False)
	
	slug_user = models.SlugField(verbose_name='URL', max_length=60, unique=True,db_index=True,blank=True)
	
	def __str__(self):
		return self.slug_user
	
	def save(self, *args, **kwargs):
		self.slug_user = slugify(self.username)+'-'+str(len(Users.objects.filter(username=self.username))+1)
		return super(Users, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
		ordering = ['username', '-confirm']
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','phone',]
	
	
	#def get_absolute_url(self):
	#	return reverse('profile', kwargs={'slug_user': self.slug_user})
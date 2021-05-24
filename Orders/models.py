from django.contrib.auth.models import Group
from django.db import models
from pytils.translit import slugify

from Users.models import Users



class Orders(models.Model):
	title = models.CharField(verbose_name='Название',unique=False,max_length=255)
	content = models.TextField(verbose_name='Описаине',unique=False)
	slug_order = models.SlugField(verbose_name='URL',max_length=255,unique=True,db_index=True,blank=True)
	pricer = models.IntegerField(verbose_name='Цена',unique=False)
	publication = models.BooleanField(verbose_name='Публикация',default=False,unique=False)
	publication_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True, unique=False)
	stage = models.IntegerField(verbose_name='Этап', default=1, unique=False)
	occupancy = models.IntegerField(verbose_name='Заполняемост', default=0, unique=False)
	photo = models.ImageField(verbose_name='Фото', upload_to='photo/orders/%Y/%m/%d', blank=True, default='default.png')
	documents = models.ImageField(verbose_name='Документы', upload_to=f'documents/{slug_order}/%Y/%m/%d', blank=True)
	categories = models.ForeignKey('Categories',verbose_name='Категории',on_delete=models.PROTECT)
	
	def __str__(self):
		return self.slug_order

	
	def save(self, *args, **kwargs):
		self.slug_order = slugify(self.title)+'-'+str(len(Orders.objects.filter(title=self.title)))
		return super(Orders, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'
		ordering = ['title', '-publication']

#   def get_absolute_url(self):
#	    return reverse('personal_area', kwargs={'slug_user': self.slug_user})

class Categories(models.Model):
	category = models.CharField(verbose_name='Категория', max_length=255, db_index=True, unique=True)
	slug_category = models.SlugField(verbose_name='URL', unique=True)
	
	def __str__(self):
		return self.category
	
	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ['category']
		

class OrderStaff(models.Model):
	categories = models.CharField(verbose_name='Категории заказов', blank=True, unique=False,max_length=255)
	rolls = models.CharField(verbose_name='Роли пользователей',blank=True, unique=False,max_length=255)
	orders = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Заказы')
	users = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Пользователи')
	
	def save(self, *args, **kwargs):
		self.rolls = Group.objects.get(user__slug_user=self.users)
		self.categories = Categories.objects.get(orders__slug_order =self.orders)
		return super(OrderStaff, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name = 'Заказ/Пользователь'
		verbose_name_plural = 'Заказы/Пользователи'
		ordering = ['id']
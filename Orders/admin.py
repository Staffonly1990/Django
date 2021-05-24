from django.contrib import admin

from Orders.models import *


class OrdersAdmin(admin.ModelAdmin):
	list_display = ('title',)
	
class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('category',)
	prepopulated_fields = {'slug_category': ('category',)}
	
class OrderStaffAdmin(admin.ModelAdmin):
	list_display = ('id','categories','rolls','orders','users')
	
	
admin.site.register(Orders,OrdersAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(OrderStaff,OrderStaffAdmin)
from django.contrib import admin

from Users.models import Users


class UsersAdmin(admin.ModelAdmin):
	list_display = ('id','username','date_joined','password','last_login','dop_info','wallet','phone','photo','email','rating','confirm','slug_user','is_staff')
	#prepopulated_fields = {'slug_user': ('username',)}

admin.site.register(Users,UsersAdmin)


from django.contrib import admin
# //from django.contrib.admin.models import Group,User
from RESTApp.models import Product
# Register your models here.
admin.site.register(Product)


admin.site.site_header='REST Project'
# admin.site.unregister(Group)
# admin.site.unregister(User)

from django.contrib import admin

# Register your models here.

from login.models import LOGIN
admin.site.register(LOGIN)

from login.models import MEMBER
admin.site.register(MEMBER)
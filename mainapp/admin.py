
# Register your models here.
from django.core.exceptions import ValidationError
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User, Group
from django.forms import *
from mainapp.forms import *


# admin.site.unregister(Group)
# admin.site.unregister(User)

# class CampainModelAdmin(admin.ModelAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         if Client.objects.filter(user=request.user).exists():
#             kwargs['exclude'] = ['signDate', 'moneySpent', 'state', 'lastUpdateDate', 'client', 'employee']
#             return super(CampainModelAdmin, self).get_form(request, obj, **kwargs)
#


admin.site.register(Client)
admin.site.register(Campaign)
admin.site.register(Service)
admin.site.register(Employee)
admin.site.register(Report)
admin.site.register(RTVResource)
admin.site.register(NonTVResource)
admin.site.register(Channel)
admin.site.register(AdvertisingPlace)
admin.site.register(Broadcast)
admin.site.register(Published)




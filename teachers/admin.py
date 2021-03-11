from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Day)
admin.site.register(Time)
admin.site.register(Schedule)
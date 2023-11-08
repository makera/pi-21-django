from django.contrib import admin
from .models import Course, Theme, Callback

admin.site.register(Course)
admin.site.register(Theme)
admin.site.register(Callback)

# Register your models here.

from django.contrib import admin

from students.models import student

class studentAdmin(admin.ModelAdmin):
	list_display = ("stdName","stdID","stdSex","stdBirth","stdEmail","stdPhone","stdAddress")
# Register your models here.
admin.site.register(student,studentAdmin)
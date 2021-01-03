from django.contrib import admin

# Register your models here.
from techsupportapp.models import Question
from techsupportapp.models import Category
from techsupportapp.models import Position
from techsupportapp.models import Division
from techsupportapp.models import Employee

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Position)
admin.site.register(Division)
admin.site.register(Employee)

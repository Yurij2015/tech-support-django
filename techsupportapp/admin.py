from django.contrib import admin

# Register your models here.
from techsupportapp.models import Question, Category, Position, Division, Employee

admin.site.register(Question)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Position)
admin.site.register(Division)
admin.site.register(Employee)

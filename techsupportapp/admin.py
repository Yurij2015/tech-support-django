from django.contrib import admin

# Register your models here.
from techsupportapp.models import Question, Category, Position, Division, Employee, Answer, QuestionStatus

admin.site.register(Question)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(QuestionStatus)
class Category(admin.ModelAdmin):
    list_display = ('question', 'status')


admin.site.register(Position)
admin.site.register(Division)
admin.site.register(Employee)
admin.site.register(Answer)

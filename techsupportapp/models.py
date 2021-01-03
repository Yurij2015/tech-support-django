from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField("Наименование категории", max_length=80)
    description = models.TextField("Описание категории")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Position(models.Model):
    name = models.CharField(max_length=40)


class Division(models.Model):
    name = models.CharField(max_length=40)


class Employee(models.Model):
    name = models.CharField(max_length=80)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)


class Question(models.Model):
    customer = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()
    answerDate = models.DateField()
    status = models.IntegerField()
    user = models.IntegerField()
    division = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

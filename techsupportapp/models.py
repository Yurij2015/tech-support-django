from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    answerDate = models.DateField()
    status = models.IntegerField()
    user = models.IntegerField()
    division = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()


class Employee(models.Model):
    name = models.CharField(max_length=40)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)


class Position(models.Model):
    name = models.CharField(max_length=40)


class Division(models.Model):
    name = models.CharField(max_length=40)


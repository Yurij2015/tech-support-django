from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    user = models.IntegerField()
    category = models.IntegerField()
    division = models.IntegerField()






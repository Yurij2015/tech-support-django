from datetime import datetime

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
        verbose_name = "категорию"
        verbose_name_plural = "категории"


class Position(models.Model):
    name = models.CharField("Наименование должности", max_length=40)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    class Meta:
        verbose_name = "должность"
        verbose_name_plural = "должности"


class Division(models.Model):
    name = models.CharField("Наименование отдела", max_length=40)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    class Meta:
        verbose_name = "отдел"
        verbose_name_plural = "отделы"


class Employee(models.Model):
    name = models.CharField("ФИО сотрудника", max_length=80)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Должность")
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name="Отдел")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    class Meta:
        verbose_name = "сотрудника"
        verbose_name_plural = "сотрудники"


class Question(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    questionName = models.CharField("Название заявки", max_length=100, null=True)
    question = models.TextField("Содержание заявки", null=True)
    questionDate = models.DateTimeField("Дата создания заявки", null=True, blank=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name="Отдел")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.questionName

    class Meta:
        verbose_name = "заявку"
        verbose_name_plural = "заявки"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Заявка")
    answer = models.TextField("Ответ по заявке")
    answerDate = models.DateField("Дата ответа")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.answer

    class Meta:
        verbose_name = "ответ по заявке"
        verbose_name_plural = "ответы по заявкам"


class QuestionStatus(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Заявка")
    status = models.IntegerField("Статус заявки")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.status

    class Meta:
        verbose_name = "статус заявки"
        verbose_name_plural = "статусы заявок"

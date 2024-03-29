# Generated by Django 3.1.7 on 2021-03-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techsupportapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категорию', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='Описание категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Наименование категории'),
        ),
    ]

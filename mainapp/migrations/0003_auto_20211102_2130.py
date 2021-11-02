# Generated by Django 3.2.7 on 2021-11-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_summer_winter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summer',
            name='size',
            field=models.CharField(choices=[('39', '39'), ('41', '41'), ('43', '43'), ('45', '45')], default='41', max_length=2, verbose_name='Размер обуви'),
        ),
        migrations.AlterField(
            model_name='winter',
            name='size',
            field=models.CharField(choices=[('39', '39'), ('41', '41'), ('43', '43'), ('45', '45')], default='41', max_length=2, verbose_name='Размер обуви'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-11-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20211103_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='size',
            field=models.CharField(choices=[('39', '39'), ('41', '41'), ('43', '43'), ('45', '45')], default=None, max_length=2, verbose_name='Размер обуви'),
        ),
    ]

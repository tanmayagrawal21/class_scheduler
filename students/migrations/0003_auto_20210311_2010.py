# Generated by Django 3.1.5 on 2021-03-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20210311_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.IntegerField(default=0),
        ),
    ]

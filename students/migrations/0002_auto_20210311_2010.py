# Generated by Django 3.1.5 on 2021-03-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='board',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='standard',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

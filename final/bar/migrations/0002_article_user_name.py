# Generated by Django 3.2.5 on 2021-07-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

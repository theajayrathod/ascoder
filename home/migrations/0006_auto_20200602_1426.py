# Generated by Django 3.0.6 on 2020-06-02 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_createpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createpost',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='createpost',
            name='timeStamp',
        ),
    ]

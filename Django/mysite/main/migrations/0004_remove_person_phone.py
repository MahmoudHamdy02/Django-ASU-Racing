# Generated by Django 3.2.7 on 2021-09-15 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_person_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='phone',
        ),
    ]
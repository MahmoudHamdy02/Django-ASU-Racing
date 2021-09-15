# Generated by Django 3.2.7 on 2021-09-15 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0005_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
            ],
        ),
    ]

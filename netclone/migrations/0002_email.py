# Generated by Django 3.1.7 on 2021-07-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netclone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
# Generated by Django 4.2.7 on 2024-01-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('explain', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=256)),
                ('date', models.CharField(max_length=256)),
            ],
        ),
    ]
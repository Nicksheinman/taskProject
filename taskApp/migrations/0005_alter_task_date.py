# Generated by Django 4.2.7 on 2024-03-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0004_delete_user_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.CharField(max_length=256),
        ),
    ]

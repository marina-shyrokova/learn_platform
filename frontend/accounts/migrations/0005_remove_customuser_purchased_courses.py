# Generated by Django 5.0.2 on 2024-03-01 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_purchased_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='purchased_courses',
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_purchased_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='purchased_courses',
            field=models.JSONField(default=list),
        ),
    ]

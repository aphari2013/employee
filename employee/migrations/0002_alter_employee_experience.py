# Generated by Django 4.0.4 on 2022-06-10 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='experience',
            field=models.PositiveIntegerField(null=True),
        ),
    ]

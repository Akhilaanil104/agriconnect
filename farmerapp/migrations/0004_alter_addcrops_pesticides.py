# Generated by Django 4.2.7 on 2023-11-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0003_addcrops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcrops',
            name='pesticides',
            field=models.TextField(),
        ),
    ]

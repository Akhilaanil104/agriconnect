# Generated by Django 4.2.7 on 2023-11-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyScheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('eligibility', models.TextField()),
                ('reqdocs', models.TextField()),
                ('ldate', models.DateField()),
            ],
        ),
    ]

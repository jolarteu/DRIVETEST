# Generated by Django 4.0.4 on 2022-05-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0002_alter_drivetest_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivetest',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='drivetest',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]

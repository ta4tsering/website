# Generated by Django 3.2.13 on 2022-05-08 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0007_auto_20220508_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherprofile',
            old_name='price_per_hour',
            new_name='fee_per_hour',
        ),
    ]

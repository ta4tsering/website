# Generated by Django 3.2.13 on 2022-05-07 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_auto_20220507_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherprofile',
            old_name='work_experience',
            new_name='bio',
        ),
    ]

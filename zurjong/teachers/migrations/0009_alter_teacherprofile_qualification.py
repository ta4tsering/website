# Generated by Django 3.2.13 on 2022-05-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0008_rename_price_per_hour_teacherprofile_fee_per_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='qualification',
            field=models.TextField(),
        ),
    ]

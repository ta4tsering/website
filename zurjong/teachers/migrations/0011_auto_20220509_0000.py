# Generated by Django 3.2.13 on 2022-05-08 18:30

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0010_auto_20220508_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='bio',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='contact_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='curriculums',
            field=models.ManyToManyField(blank=True, null=True, to='teachers.Curriculum'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='fee_per_hour',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='languages',
            field=models.ManyToManyField(blank=True, null=True, to='teachers.Language'),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='qualification',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacherprofile',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to='teachers.StudentAgeRange'),
        ),
    ]
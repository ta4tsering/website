# Generated by Django 3.2.13 on 2022-05-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAgeRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('low', models.IntegerField()),
                ('high', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeachingSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(max_length=13)),
                ('qualification', models.TextField(max_length=30)),
                ('work_experience', models.TextField()),
                ('comfortable_with_english', models.BooleanField(default=False)),
                ('price_per_hour', models.IntegerField(default=0)),
                ('can_teach_to_student', models.ManyToManyField(to='teachers.StudentAgeRange')),
                ('teaching_subjects', models.ManyToManyField(to='teachers.TeachingSubject')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-08-21 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_courses_teacher'),
        ('student', '0004_student_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='courses.courses'),
        ),
    ]

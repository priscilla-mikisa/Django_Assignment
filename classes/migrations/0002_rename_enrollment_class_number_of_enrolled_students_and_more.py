# Generated by Django 5.0.6 on 2024-07-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='enrollment',
            new_name='number_of_enrolled_students',
        ),
        migrations.RemoveField(
            model_name='class',
            name='class_time',
        ),
        migrations.RemoveField(
            model_name='class',
            name='course',
        ),
        migrations.RemoveField(
            model_name='class',
            name='room_number',
        ),
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
        migrations.AddField(
            model_name='class',
            name='names_of_teachers',
            field=models.TextField(default='canary'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class',
            name='number_of_classrooms',
            field=models.TextField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class',
            name='meeting_days',
            field=models.CharField(max_length=20),
        ),
    ]

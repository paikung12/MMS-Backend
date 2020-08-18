# Generated by Django 3.0.8 on 2020-08-16 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseManagementSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.CharField(max_length=20)),
                ('NameCourse', models.CharField(max_length=200)),
                ('TeachingPeriod', models.DateTimeField()),
                ('TeacherName', models.CharField(max_length=200)),
                ('CourseStatus', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MemberManagementSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudenID', models.CharField(max_length=20)),
                ('CourseIDEnroll', models.CharField(max_length=200)),
                ('Enrolldate', models.DateTimeField()),
                ('Name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=250)),
                ('ContactDetails', models.CharField(max_length=200)),
                ('ParentContac', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MMSadmin.CourseManagementSystem')),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-26 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Staff_Id', models.CharField(max_length=100, null=True)),
                ('Staff_Name', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=100, null=True)),
                ('Email', models.CharField(max_length=100, null=True)),
                ('Contact_No', models.CharField(max_length=100, null=True)),
                ('Gender', models.CharField(max_length=100, null=True)),
                ('DOB', models.CharField(max_length=100, null=True)),
                ('Upload_photo', models.CharField(max_length=100, null=True)),
                ('Course', models.CharField(max_length=100, null=True)),
                ('Semester', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
# Generated by Django 4.0.3 on 2022-05-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecafe', '0005_remove_faculty_address_remove_faculty_contact_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, null=True)),
                ('password', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]

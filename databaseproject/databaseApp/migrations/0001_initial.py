# Generated by Django 4.1 on 2022-09-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=30)),
                ('saddress', models.CharField(max_length=200)),
                ('doj', models.DateField()),
            ],
        ),
    ]

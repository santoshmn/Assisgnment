# Generated by Django 2.2 on 2019-04-24 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=1000)),
                ('Specialty', models.CharField(max_length=500)),
                ('Years_of_Experience', models.IntegerField()),
                ('Photo', models.ImageField(upload_to='')),
                ('Availability', models.TimeField()),
            ],
        ),
    ]
# Generated by Django 2.2 on 2019-04-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_auto_20190424_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Availability',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 2.2.16 on 2020-11-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0008_remove_temperature_date_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='date_taken',
            field=models.DateTimeField(null=True),
        ),
    ]

# Generated by Django 2.2.16 on 2020-11-14 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0007_delete_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temperature',
            name='date_taken',
        ),
    ]

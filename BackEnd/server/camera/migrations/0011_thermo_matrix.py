# Generated by Django 2.2.19 on 2021-03-03 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0010_auto_20201116_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='thermo',
            name='matrix',
            field=models.TextField(null=True),
        ),
    ]
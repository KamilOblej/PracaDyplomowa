# Generated by Django 2.2.16 on 2020-11-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='data',
            name='temperature1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='temperature2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='thermo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
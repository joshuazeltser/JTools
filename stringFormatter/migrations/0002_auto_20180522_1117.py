# Generated by Django 2.0.3 on 2018-05-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stringFormatter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='text_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='result',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
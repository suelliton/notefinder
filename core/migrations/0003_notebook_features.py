# Generated by Django 2.2.4 on 2019-08-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190819_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='features',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
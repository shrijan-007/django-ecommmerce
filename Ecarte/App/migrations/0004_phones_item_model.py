# Generated by Django 3.2.8 on 2021-11-14 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20211112_0526'),
    ]

    operations = [
        migrations.AddField(
            model_name='phones',
            name='Item_model',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
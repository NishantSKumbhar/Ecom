# Generated by Django 4.0.3 on 2022-05-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img_url',
            field=models.CharField(default='', max_length=2010),
        ),
    ]

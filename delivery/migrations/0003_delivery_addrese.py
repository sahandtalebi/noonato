# Generated by Django 4.0.1 on 2022-02-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_alter_delivery_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='addrese',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bakery',
            name='bread_type',
            field=models.CharField(choices=[('Barbary', 'بربری'), ('sangak', 'سنگک'), ('lavash', 'لواش'), ('fantasy', 'فانتزی'), ('tafton', 'تافتون'), ('more', 'متفرقه')], default=1, max_length=20, verbose_name='نوع نان تولیدی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bakery',
            name='order_count',
            field=models.IntegerField(default=0, verbose_name='تعداد کل سفارشات نان'),
        ),
        migrations.AddField(
            model_name='bakery',
            name='today_order',
            field=models.IntegerField(default=0, verbose_name='تعداد سفارشات امروز'),
        ),
    ]

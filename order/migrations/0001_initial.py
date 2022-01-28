# Generated by Django 4.0.1 on 2022-01-28 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bakery', '0002_bakery_bread_type_bakery_order_count_and_more'),
        ('delivery', '0002_alter_delivery_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=30, verbose_name='کد سفارش')),
                ('full_name', models.CharField(max_length=120, verbose_name='نام و نام خانوادگی')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('post_code', models.IntegerField(default=0, verbose_name='کدپستی')),
                ('map_address', models.URLField(blank=True, null=True, verbose_name='نقشه گوگل')),
                ('order_type', models.CharField(choices=[('barbary', 'بربری'), ('sangak', 'سنگک'), ('lavash', 'لواش'), ('fantasy', 'فانتزی'), ('tafton', 'تافتون'), ('more', 'متفرقه')], max_length=20, verbose_name='نوع نان')),
                ('order_count', models.IntegerField(default=1, verbose_name='تعداد سفارشات')),
                ('internet_pay', models.BooleanField(default=True, verbose_name='پرداخت اینترنتی')),
                ('order_price', models.IntegerField(default=0, verbose_name='پول پرداختی')),
                ('status', models.CharField(choices=[('false', 'انتظار تایید پیک'), ('in_road', 'تو راهم'), ('true', 'رسید دستش')], default=('in_road', 'تو راهم'), max_length=30, verbose_name='وضعیت')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('bakery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bakery.bakery', verbose_name='نانوا')),
                ('delivery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery.delivery', verbose_name='پیک')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
            },
        ),
    ]

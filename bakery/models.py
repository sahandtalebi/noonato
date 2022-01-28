from django.db import models
from django.contrib.auth.models import User


class Bakery(User):

    BREAD_TYPE = [
        ('Barbary', 'بربری'),
        ('sangak', 'سنگک'),
        ('lavash', 'لواش'),
        ('fantasy', 'فانتزی'),
        ('tafton', 'تافتون'),
        ('more', 'متفرقه'),
    ]

    shop_name = models.CharField(max_length=120, verbose_name='اسم مغازه')
    phone_number = models.CharField(max_length=20, verbose_name='شماره همراه')
    shop_phone = models.CharField(max_length=20, verbose_name='شماره ثابت')
    work_time = models.CharField(max_length=200, verbose_name='ساعت کاری')
    morning_work = models.BooleanField(default=True, verbose_name='کار صبح')
    bread_type = models.CharField(choices=BREAD_TYPE, max_length=20,verbose_name='نوع نان تولیدی')
    today_order = models.IntegerField(verbose_name='تعداد سفارشات امروز', default=0)
    order_count = models.IntegerField(verbose_name='تعداد کل سفارشات نان', default=0)

    def __str__(self):
        return f'{self.shop_name}, {self.get_full_name()}'

    class Meta:
        verbose_name ='نانوایی'
        verbose_name_plural = 'نانوایی ها'
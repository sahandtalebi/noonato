from datetime import datetime
from django.db import models
from bakery.models import Bakery
from delivery.models import Delivery
from lib.models import BaseModel


class Order(BaseModel):
    BREAD_TYPE = [
        ('barbary', 'بربری'),
        ('sangak', 'سنگک'),
        ('lavash', 'لواش'),
        ('fantasy', 'فانتزی'),
        ('tafton', 'تافتون'),
        ('more', 'متفرقه'),
    ]
    STATUS = [
        ('waiting', 'انتظار تایید پیک'),
        ('accepted', 'تو راهم'),
        ('received', 'رسید دستش'),
    ]
    bakery = models.ForeignKey(Bakery, on_delete=models.SET_NULL,
                               verbose_name='نانوا', null=True, )
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL, verbose_name='پیک', null=True, blank=True)

    order_code = models.CharField(max_length=30, verbose_name='کد سفارش')
    full_name = models.CharField(max_length=120, verbose_name='نام و نام خانوادگی')
    address = models.TextField(verbose_name='آدرس')
    post_code = models.IntegerField(verbose_name='کدپستی', default=0)
    map_address = models.URLField(verbose_name='نقشه گوگل', blank=True, null=True)

    order_type = models.CharField(choices=BREAD_TYPE, max_length=20, verbose_name='نوع نان')
    order_count = models.IntegerField(verbose_name='تعداد سفارشات', default=1)

    internet_pay = models.BooleanField(default=True, verbose_name='پرداخت اینترنتی')
    order_price = models.IntegerField(default=0, verbose_name='پول پرداختی')

    status = models.CharField(choices=STATUS, max_length=30, verbose_name='وضعیت')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return f'{self.full_name}, {self.order_code}, {self.status}'

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

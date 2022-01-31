from django.shortcuts import render
from order.models import Order


def order_view(request):

    open_order = Order.objects.filter(delivery=None)
    context = {
        'open_order': open_order,
    }
    return render(request, 'order_template.html', context)

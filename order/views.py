from django.shortcuts import render
from order.models import Order


def order_view(request):
    user = request.user
    print(user)
    open_order = Order.objects.filter(status='waiting')
    print(open_order)
    accepted_order = Order.objects.filter(delivery__username=user.username, status='accepted')
    print(accepted_order)
    ended_order = Order.objects.filter(delivery__username=user.username, status='received')
    print(ended_order)

    context = {
        'open_order': open_order,
        'accepted_order': accepted_order,
        'ended_order': ended_order,
    }
    return render(request, 'order_template.html', context)

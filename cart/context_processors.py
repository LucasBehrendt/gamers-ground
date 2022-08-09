from decimal import Decimal
from django.conf import settings


def cart_contents(request):
    """Context processor for cart data"""
    cart_items = [0]
    total = 0
    product_count = 0
    standard_delivery = Decimal(7.99)

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = standard_delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'standard_delivery': standard_delivery,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

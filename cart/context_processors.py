from decimal import Decimal, ROUND_DOWN
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """Context processor for cart data"""
    cart_items = []
    total = 0
    product_count = 0
    # Quantize source: https://docs.python.org/3/library/decimal.html
    standard_delivery = Decimal(7.99).quantize(
        Decimal('.01'), rounding=ROUND_DOWN)
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        item_total = quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'item_total': item_total,
            'quantity': quantity,
            'product': product,
        })

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

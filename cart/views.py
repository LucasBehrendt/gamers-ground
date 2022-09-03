from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.views import generic
from products.models import Product


class ViewCart(generic.TemplateView):
    """Renders the cart page with saved items"""
    template_name = 'cart/cart.html'


class AddToCart(generic.View):
    """
    Adds product to cart. If it already exists in cart,
    increments qty by one.
    """
    def post(self, request, item_id):

        item = get_object_or_404(Product, pk=item_id)
        redirect_url = request.POST.get('redirect_url')
        cart = request.session.get('cart', {})

        if item_id in list(cart.keys()):
            cart[item_id] += 1
            messages.success(
                request, f'Updated {item.name} quantity to \
                {cart[item_id]} in your cart!', extra_tags='show-cart')
        else:
            cart[item_id] = 1
            messages.success(
                request, f'Added {item.name} to your cart!',
                extra_tags='show-cart')

        request.session['cart'] = cart
        return redirect(redirect_url)


class EditCart(generic.View):
    """
    Sets product qty to user input in cart.
    If input is 0, removes from cart.
    """
    def post(self, request, item_id):

        item = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {item.name} quantity to \
                {cart[item_id]} in your cart!', extra_tags='show-cart')
        else:
            del cart[item_id]
            messages.success(
                request, f'Removed {item.name} from your cart!',
                extra_tags='show-cart')

        request.session['cart'] = cart
        return redirect('view_cart')


class DeleteFromCart(generic.View):
    """
    Delete product from cart.
    If product not found in cart, display error message.
    """
    def get(self, request, item_id):

        try:
            item = get_object_or_404(Product, pk=item_id)
            cart = request.session.get('cart', {})

            del cart[item_id]
            messages.success(
                request, f'Removed {item.name} from your cart!',
                extra_tags='show-cart')

            request.session['cart'] = cart
            return redirect('view_cart')
        except Exception as e:
            messages.error(
                request, f'Error removing item: {e}', extra_tags='show-cart')
            return redirect('view_cart')

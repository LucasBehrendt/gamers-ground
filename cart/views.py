from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from products.models import Product


class ViewCart(generic.TemplateView):
    """Renders the cart page with saved items"""
    template_name = 'cart/cart.html'


class AddToCart(generic.View):
    """Adds product to cart"""
    def post(self, request, item_id):

        redirect_url = request.POST.get('redirect_url')
        cart = request.session.get('cart', {})

        if item_id in list(cart.keys()):
            cart[item_id] += 1
        else:
            cart[item_id] = 1

        request.session['cart'] = cart
        return redirect(redirect_url)


class EditCart(generic.View):
    """Edits product in cart"""
    def post(self, request, item_id):

        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

        if quantity > 0:
            cart[item_id] = quantity
        else:
            del cart[item_id]

        request.session['cart'] = cart
        return redirect('view_cart')


class DeleteFromCart(generic.View):
    """Delete product from cart"""
    def get(self, request, item_id):

        try:
            deleted_item = get_object_or_404(Product, pk=item_id)
            cart = request.session.get('cart', {})

            del cart[item_id]

            request.session['cart'] = cart
            return redirect('view_cart')
        except Exception as e:
            return redirect('view_cart')

from django.shortcuts import render, redirect
from django.views import generic


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

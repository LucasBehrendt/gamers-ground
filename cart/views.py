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
        print(request.session['cart'])
        return redirect(redirect_url)

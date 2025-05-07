from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from cart.contexts import cart_contents


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in cart at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RLpIhCyGRl4qoSjxoCY5BupZEGIFvzmuc3nnb8gZiCFTmEaXHT1GpuMm85GVEjOMxE04kiQP11U0DAef6TV2i7V00vDGrVPg3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

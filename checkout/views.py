from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51R1SsO4CudYZNQaNoi0nz7DTMN9JU9GHDeyWqsSeArpEtmzLmeG8j7lJc64oYjx1GAK2L9DxYFG3inC6hI9YoJ2p00THhYfK2y',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

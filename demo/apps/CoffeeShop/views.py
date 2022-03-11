from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.forms import inlineformset_factory, modelformset_factory
from demo.apps.users.models import User
from .models import CoffeeStore, CoffeeOrder
from .formsets import BaseOrderFormSet
from .utils import *


# Create your views here.
def OrderStore(request):
    # OrderFormSet = modelformset_factory(Coffee, fields=['name', 'size', 'quantity'], max_num=3, extra=3)
    OrderFormSet = modelformset_factory(CoffeeStore, fields=['name', 'size', 'quantity'], max_num=10, extra=3, validate_max=True, can_delete=True)
    if request.method == 'POST':
        order_formset = OrderFormSet(request.POST)
        if order_formset.is_valid():
            order_formset.save()
            # return redirect('dashboard')
            return HttpResponseRedirect('/dashboard')
    else:
        # order_formset= OrderFormSet()
        # order_formset= OrderFormSet(initial=[
        #     {'name': AMERICANO, 'size': LARGE, 'quantity': '1'},
        #     {'name': CAPPUCCINO, 'size': LARGE, 'quantity': '1'},
        #     {'name': COLD, 'size': LARGE, 'quantity': '1'}
        # ], queryset=Coffee.objects.none())
        data = {
            'form-TOTAL_FORMS': '3',
            'form-INITIAL_FORMS': '0',
            'form-0-name': AMERICANO,
            'form-0-quantity': '1',
            'form-0-size': LARGE,
            'form-1-name': CAPPUCCINO,
            'form-1-quantity': '1',
            'form-1-size': LARGE,
            'form-2-name': COLD,
            'form-2-quantity': '1',
            'form-2-size': LARGE,
        }
        order_formset= OrderFormSet(data, queryset=CoffeeStore.objects.none())
    return render(request, 'order.html', {'formset': order_formset})


def PlaceOrder(request):
    # OrderFormSet = inlineformset_factory(User, CoffeeOrder, fields=['name', 'size', 'quantity'], max_num=5, extra=1, validate_max=True, can_delete=True)
    OrderFormSet = inlineformset_factory(User, CoffeeOrder, formset=BaseOrderFormSet, fields=['name', 'size', 'quantity'], max_num=5, extra=1, validate_max=True, can_delete=True)
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        order_formset = OrderFormSet(request.POST, instance=user)
        if order_formset.is_valid():
            order_formset.save()
            # return redirect('dashboard')
            return HttpResponseRedirect('/dashboard')
    else:
        # order_formset= OrderFormSet(initial=[
        #     {'name': AMERICANO, 'size': LARGE, 'quantity': '1'},
        # ], queryset=CoffeeOrder.objects.none(), instance=user)
        
        order_formset= OrderFormSet(queryset=CoffeeOrder.objects.none(), instance=user)
    return render(request, 'order.html', {'formset': order_formset})

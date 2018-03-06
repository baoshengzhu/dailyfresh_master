#coding: utf-8

from django.shortcuts import render

def df_cart(request):
    return render(request, 'cart.html')



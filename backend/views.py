from django.shortcuts import render

def shoplist(request):
    return render(request, 'shop-list.html')

def shopsingle(request):
    return render(request, 'shop-single.html')
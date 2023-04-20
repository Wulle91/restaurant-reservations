from django.shortcuts import render, redirect
from django.views import generic, View
from .models import  Date

# Create your views here.
def say_hello(request):
    if request.method == 'POST':
        reservation_date = request.POST.get('reservation_date')
        table = request.POST.get('Table')    
        Date.objects.create(reservation_date=reservation_date, table=table)
        return redirect(say_hello)
    return render(request, 'base.html')
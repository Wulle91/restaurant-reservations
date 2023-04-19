from django.shortcuts import render
from django.views import generic, View
from .models import Reservation, Date

# Create your views here.
def reservations(request):
    items = Date.objects.all()
    context = {
        'items': items
    }
    return render(request, 'index.html', context)


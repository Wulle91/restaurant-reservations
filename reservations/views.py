from django.shortcuts import render

from .models import Date, Reservation

# Create your views here.

def sho_dates(request):
    dates = Date.objects.all()
    reservations = Reservation.objects.all()
    context = {
        'dates': dates,
        'reservations': reservations
    }
    if request.method == 'POST':
        reservation_date = request.POST.get('reservation_date')
        table = request.POST.get('Table')    
        name = request.POST.get('name')
        email = request.POST.get('email')    
        phone_number = request.POST.get('phone')  
        comment = request.POST.get('comment')  
        Reservation.objects.create(name=name, email=email, phone_number=phone_number, comment=comment)
        Date.objects.get_or_create(reservation_date=reservation_date, table=table, checked=True)
    return render(request, 'index.html', context)


def comments(request):
    return render(request, 'home.html')

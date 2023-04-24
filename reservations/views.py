from django.shortcuts import render

from .models import Date

# Create your views here.
def pick_a_date_and_table(request):
    if request.method == 'POST':
        reservation_date = request.POST.get('reservation_date')
        table = request.POST.get('Table')    
        Date.objects.get_or_create(reservation_date=reservation_date, table=table, checked=True)
        return redirect(pick_a_date_and_table)
    return render(request, 'index.html')



def sho_dates(request):
    dates = Date.objects.all()
    context = {
        'dates': dates
    }
    if request.method == 'POST':
        reservation_date = request.POST.get('reservation_date')
        table = request.POST.get('Table')    
        Date.objects.get_or_create(reservation_date=reservation_date, table=table, checked=True)
    return render(request, 'index.html', context)

from django.shortcuts import render

from .models import Date, Reservation, Review
from .forms import CommentForm

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
    comments = Review.objects.all()
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment_form.instance.email = request.user.email
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'home.html', {
        "comments": comments,
        "comment_form": CommentForm(),
    },)
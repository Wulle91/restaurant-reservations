from django.shortcuts import render, get_object_or_404, redirect
from datetime import date
from django.contrib import messages


from .models import Date, Reservation, Review
from .forms import CommentForm


# Create your views here.

def sho_dates(request):
    dates = Date.objects.all()
    today = date.today().strftime("%Y-%m-%d")
    reservations = Reservation.objects.all()
    context = {
        'dates': dates,
        'reservations': reservations,
        'today': today,
    }
    if request.method == 'POST':
        reservation_date = request.POST.get('reservation_date')
        table = request.POST.get('Table')    
        name = request.POST.get('name')
        email = request.POST.get('email')    
        phone_number = request.POST.get('phone')  
        comment = request.POST.get('comment')  
        if reservation_date and table and name and email and phone_number:
            reservation = Reservation.objects.create(name=name, email=email, phone_number=phone_number, comment=comment)
            Date.objects.get_or_create(reservation_date=reservation_date, table=table, checked=True)
            messages.success(request, 'Your reservation has been successfully created!')
            return redirect('home')
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
    
    
def delete_comment(request, comment_id):
    comment = get_object_or_404(Review, id=comment_id)
    comment.delete()
    return redirect('home')

def delete_reservation(request, date_id):
    reservation_id = int(date_id) + 164
    reservation = get_object_or_404(Reservation, id=reservation_id)
    date = get_object_or_404(Date, id=date_id)
    reservation.delete()
    date.delete()
    return redirect('home')


def edit_reservation(request, date_id):
    reservation_id = int(date_id) + 164
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation.phone_number = request.POST.get('new_phone_number')  
        reservation.comment = request.POST.get('new_comment')  
        reservation.save()

        # redirect to success page or somewhere else
        return redirect('home')

    context = {'reservation': reservation,
               'default_phone_number': reservation.phone_number,
               'default_comment': reservation.comment,
               'reservation_id': reservation_id,
               }
    return render(request, 'index.html', context)
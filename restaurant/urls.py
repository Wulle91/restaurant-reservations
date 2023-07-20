from django.contrib import admin
from django.urls import path, include
from reservations.views import sho_dates, comments, delete_comment, edit_reservation, delete_reservation

urlpatterns = [
    path('edit/<date_id>', edit_reservation, name='edit'),
    path('delete_comment/<comment_id>', delete_comment, name='delete_comment'),
    path('delete/<date_id>', delete_reservation, name='delete'),
    path('admin/', admin.site.urls),
    path('', comments, name='home'),
    path('accounts/', include('allauth.urls')),
    path('reservations', sho_dates, name='dates'),
]

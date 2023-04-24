from django.contrib import admin
from .models import Reservation, Date
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Date)

#admin.site.register(Reservation)

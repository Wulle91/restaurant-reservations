from django.contrib import admin
from .models import Reservation, Date
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reservation, Date)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

#admin.site.register(Reservation)

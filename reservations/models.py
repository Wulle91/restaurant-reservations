from django.db import models
from django.core.validators import RegexValidator

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    staus = models.IntegerField(choices=STATUS, default=0)


class Date(models.Model):
    reservation_date = models.DateTimeField()
    table = models.ForeignKey(Reservation, on_delete=models.CASCADE)

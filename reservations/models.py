from django.db import models
from django.core.validators import RegexValidator

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    staus = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return f"Reservation for {self.name}"


TABLES = ((0, "none"),
          (1, "Table1"),
          (2, "Table2"),
          (3, "Table3"),
          (4, "Table4"),
          (5, "Table5"))

class Date(models.Model):
    reservation_date = models.DateTimeField()
    table = models.IntegerField(choices=TABLES, default=0)
    checked = models.BooleanField(null=False, blank=False, default=False)
    
    class Meta:
        unique_together = [["reservation_date", "table"]]


class Review(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        
    def __str__(self):
        return f"Comment {self.body} by {self.name}"
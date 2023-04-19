from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    table = models.TextChoices("table", "table1 table2 table3 table4 table5")
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    staus = models.IntegerField(choices=STATUS, default=0)

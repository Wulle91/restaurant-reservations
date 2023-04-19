from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField()
    TABLE1 = "Table1"
    TABLE2 = "Table2"
    TABLE3 = "Table3"
    TABLE4 = "Table4"
    TABLE5 = "Table5"
    LIST_OF_TABLES = [
        (TABLE1, "Table1"),
        (TABLE2, "Table2"),
        (TABLE3, "Table3"),
        (TABLE4, "Table4"),
        (TABLE5, "Table5"),
    ]
    table = models.CharField(
        max_length=6,
        choices=LIST_OF_TABLES,
        default=None,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    staus = models.IntegerField(choices=STATUS, default=0)

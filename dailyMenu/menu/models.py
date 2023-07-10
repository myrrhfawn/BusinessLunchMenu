from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    DAYS = (
        ('Mon', "Monday"),
        ('Tue', "Tuesday"),
        ('Wed', "Wednesday"),
        ('Thu', "Thursday"),
        ('Fri', "Friday"),
        ('Sat', "Saturday"),
        ('Sun', "Sunday")
    )
    days = MultiSelectField(choices=DAYS, max_length=255, default='Mon')

    def __str__(self):
        return self.title

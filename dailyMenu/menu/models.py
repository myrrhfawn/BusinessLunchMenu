from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
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


class Order(models.Model):
    user_id = models.IntegerField()
    dish_id = models.ForeignKey('Menu', on_delete=models.PROTECT, null=True)

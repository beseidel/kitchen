from django.db import models

# Create your models here.
class Cart(models.Model):
    item_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    menu_id = models.ForeignKey()

    def __str__(self):
        return self.item_name

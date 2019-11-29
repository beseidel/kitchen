from django.db import models
from django.urls import reverse

class Buyer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    question_1 = models.CharField(max_length=100)
    question_2 = models.CharField(max_length=100)
    answer_1 = models.CharField(max_length=20)
    answer_2 = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name+ ' ' + self.last_name

class Kitchen(models.Model):
    kitchen_id = models.IntegerField(primary_key=True)
    kitchen_name = models.CharField(max_length=50)
    working_days = models.IntegerField(null = True)
    working_start_time = models.TimeField(auto_now=False)
    working_end_time = models.TimeField(auto_now=False)
    kitchen_image = models.ImageField( blank=True, null=True)
    menu = models.ListCharField( size=None)
    provider_id = models.ForeignKey()

    def __str__(self):
        return self.kitchen_name
    #add dish to menue(self,dish)

class Provider(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    question_1 = models.CharField(max_length=100)
    question_2 = models.CharField(max_length=100)
    answer_1 = models.CharField(max_length=20)
    answer_2 = models.CharField(max_length=20)
    #add_item_to_menue(self,item)
    def __str__(self):
        return self.first_name+ ' ' + self.last_name

class WorkingDay(models.Model):
    day = models.IntegerField()
    kitchen_id = models.ForeignKey()

    def __str__(self):
        return self.kitchen_id + ':'+self.day

class Menu(models.Model):
    item_name= models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_vegan = models.BooleanField(null=True)
    kitchen_id = models.ForeignKey()

    def __str__(self):
        return self.item_name
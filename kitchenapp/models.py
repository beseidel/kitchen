from django.db import models
# Create your models here.


class Provider(models.Model):
   first_name = models.CharField(max_length=20, null=False)
   last_name = models.CharField(max_length=20, null=False)
   password = models.CharField(max_length=10, null=False)
   question_1 = models.CharField(max_length=100, default='NA', null=False)
   question_2 = models.CharField(max_length=100, default='NA', null=False)
   answer_1 = models.CharField(max_length=20, null=False)
   answer_2 = models.CharField(max_length=20, null=False)


class Buyer(models.Model):
   first_name = models.CharField(max_length=20, null=False)
   last_name = models.CharField(max_length=20, null=False)
   password = models.CharField(max_length=10, null=False)
   question_1 = models.CharField(max_length=100, default='What is your favorite color?', null=False)
   question_2 = models.CharField(max_length=100, default='Who is your best friend?', null=False)
   answer_1 = models.CharField(max_length=20, null=False)
   answer_2 = models.CharField(max_length=20, null=False)



class Kitchen(models.Model):
   kitchen_name = models.CharField(max_length=50, null=False, default="NA")
   #working_days = []
   image_url = models.CharField(max_length=200)
   provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=False)

class WorkingDay(models.Model):
   day = models.CharField(max_length=15, null=False, default='NA')
   start_time = models.CharField(max_length=10, null=False, default='NA') 
   end_time = models.CharField(max_length=10, null=False, default='NA') 

   kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)

class Menu(models.Model):
   dish_name = models.CharField(max_length=50, null=False, default='N/A')
   price =  models.DecimalField(max_digits=4, decimal_places=2, null=False)
   is_vegan = models.BooleanField(default=False)

   kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, null=False)



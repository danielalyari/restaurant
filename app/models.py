from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator,MinValueValidator,MaxValueValidator
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser


class FoodType(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.title}"
    

class Food (models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255,blank=True)
    weight = models.PositiveIntegerField(null =True,blank=True)
    #length = models.PositiveIntegerField
    description= models.TextField(blank=True)
    old_price = models.PositiveBigIntegerField(null=True,blank=True)
    price = models.PositiveBigIntegerField()
    image =  models.ImageField(upload_to="foods/")
    food_types = models.ManyToManyField(to=FoodType)
    
    

     
class SuggestionsCritics(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=11, blank=True, validators=[MinLengthValidator(11, "کمتر از 11 رقم وارد نکنید."), MaxLengthValidator(11, "بیشتر از 11 رقم وارد نکنید")])
    text = models.TextField()
      
      
      
class Order(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=11,validators=[MinLengthValidator(11,"کمتر از  11 رقم وارد نکنید ."),MaxLengthValidator ("11,بیشتر از 11 رقم وارد نکنید ")])
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1,"سفارش باید بیش از یک عدد باشه"),MaxValueValidator(10,"سفارش باید کمتر  از 11 عدد باشه ")])
    
    
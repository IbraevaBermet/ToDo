from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class ToMeet(models.Model):
    persone = models.CharField(max_length=100)
    phone_number =models.CharField(max_length=15) 
    date_of_meeting= models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class Habits(models.Model):
    name = models.CharField(max_length=100)
    done_for_today = models.CharField(max_length=200)
    important =  models.CharField(max_length=300)
    comment = models.CharField(max_length=400)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

        

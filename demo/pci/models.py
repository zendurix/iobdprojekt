from django.db import models

# Create your models here.

# regular class
class Price:
    id : int
    value : int
    desc : str
    difficult : bool

#a model, more powerful class
class TestingClass(models.Model):
    #this time we use = instead of :
    name = models.CharField(max_length=20)
    desc = models.TextField()
    value = models.IntegerField
    living = models.BooleanField(default=False)
    img = models.ImageField(upload_to = 'pics',)

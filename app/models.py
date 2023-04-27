from django.db import models
from django.core import validators
# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,validators=[validators.MaxLengthValidator(10)])
    def __str__(self):
        return self.topic_name
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,primary_key=True,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(4)])
    email=models.EmailField()
    url=models.URLField()
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(4)])
    date=models.DateField()
    def __str__(self):
        return self.author
    
   
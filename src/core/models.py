from django.db import models
from django.utils import timezone

class Language(models.Model):
    """ Language model """
    name = models.CharField(max_length=25)
    abbr = models.CharField(max_length=10)

class BaseModel(models.Model):
    """ Base model for structuring all """


class Comment(models.Model):
    """ Comment model """
    text =  models.CharField(max_length=250)


class Review(models.Model):
    """ Review model """
    title = models.CharField(max_length=250)
    posted_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField()
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    view = models.IntegerField()
    video_url = models.CharField(max_length=100)
    like = models.IntegerField()


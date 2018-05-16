from django.db import models

class Attacks(models.Model):
    idNo = models.CharField(max_length=100)
    number_field = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    date = models.DateTimeField(max_length=20)
    narrative = models.CharField(max_length=250)
    town = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    deaths = models.CharField(max_length=500)
    deaths_min = models.CharField(max_length=500)
    deaths_max = models.CharField(max_length=500)
    civilians = models.CharField(max_length=500)
    injuries = models.CharField(max_length=500)
    children = models.CharField(max_length=500)
    tweet_id = models.CharField(max_length=1000)
    bureau_id = models.CharField(max_length=1000)
    bij_summary_short = models.CharField(max_length=5000)
    bij_link = models.CharField(max_length=1000)
    target = models.CharField(max_length=1000)
    lat = models.CharField(max_length=1000)
    lon = models.CharField(max_length=1000)
    articles = models.CharField(max_length=1000)
    names = models.CharField(max_length=1000)




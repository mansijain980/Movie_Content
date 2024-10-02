# movies/models.py
from django.db import models

# class Movie(models.Model):
#     title = models.CharField(max_length=255)
#     original_title = models.CharField(max_length=255)
#     original_language = models.CharField(max_length=50)
#     overview = models.TextField()
#     release_date = models.DateField(null=True, blank=True) 
#     budget = models.BigIntegerField()
#     revenue = models.BigIntegerField()
#     runtime = models.IntegerField()  # in minutes
#     status = models.CharField(max_length=50)
#     homepage = models.URLField(null=True, blank=True)
#     vote_average = models.DecimalField(max_digits=3, decimal_places=1)
#     vote_count = models.IntegerField()
#     production_company_id = models.IntegerField()
#     genre_id = models.IntegerField()
#     languages = models.CharField(max_length=255)  # assuming multiple languages as a comma-separated string
    
#     class Meta:
#         ordering = ['release_date']
class Moviescontent(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    original_language = models.CharField(max_length=50)
    overview = models.TextField()
    release_date = models.DateField(null=True, blank=True) 
    budget = models.BigIntegerField()
    revenue = models.BigIntegerField()
    runtime = models.IntegerField()  # in minutes
    status = models.CharField(max_length=50)
    homepage = models.CharField(max_length=500, null=True, blank=True)  # Increased limit for homepage
    vote_average = models.DecimalField(max_digits=3, decimal_places=1)
    vote_count = models.IntegerField()
    production_company_id = models.IntegerField()
    genre_id = models.IntegerField()
    languages = models.CharField(max_length=255)  # assuming multiple languages as a comma-separated string
    
    class Meta:
        ordering = ['release_date']


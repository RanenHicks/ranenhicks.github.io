from django.db import models

# Create your models here.

# (AppSeed, 2022), creates a model that stores the structure of an animal object.
class AnimalModel(models.Model):
    age_upon_outcome = models.CharField(max_length = 100)
    animal_id = models.CharField(max_length = 100)
    animal_type = models.CharField(max_length = 100)
    breed = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100) 
    date_of_birth = models.CharField(max_length = 100)
    datetime = models.CharField(max_length = 100)
    mothyear = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    outcome_subtype = models.CharField(max_length = 100)
    outcome_type = models.CharField(max_length = 100)
    sex_upon_outcome = models.CharField(max_length = 100)
    location_lat = models.CharField(max_length = 100)
    location_long =  models.CharField(max_length = 100)
    age_upon_outcome_in_weeks =  models.CharField(max_length = 100)
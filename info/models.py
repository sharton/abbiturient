from django.db import models
from django_countries.fields import CountryField

class GeneralInfo(models.Model):
    GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    )

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birth_date = models.DateField()
    gender = models.CharField(choices=GENDER, default='Male', max_length=10)
    country = CountryField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    how_to_know = models.CharField(max_length=150)

    def __str__(self):
        return self.last_name + self.first_name


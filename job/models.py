from datetime import *
from django.db import models
from django.contrib.auth.models import User

# import geocoder
# import os

# from django.contrib.gis.db import models as gismodels
# from django.contrib.gis.geos import Point


from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class JobType(models.TextChoices):
    Permanent = 'Permanent'
    Temporary = 'Temporary'
    InternShip = 'InternShip'


class Education(models.TextChoices):
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    Phd = 'Phd'


class Industry(models.TextChoices):
    Business = 'Business'
    It = 'Information Technology'
    Banking = 'Banking'
    Education = 'Education'
    Telecommunication = 'Telecommunication'
    Others = 'Others'


class Experience(models.TextChoices):
    No_Experience = 'No Experience'
    One_Year = '1 Year'
    Two_Year = '2 Year'
    Three_Year_Plus = '3 Year above'


def return_date_time():
    now = datetime.now()
    return now + timedelta(days=10)


class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(null=True, max_length=100)
    jobType = models.CharField(
        max_length=10,
        choices=JobType.choices,
        default=JobType.Permanent
    )
    education = models.CharField(
        max_length=10,
        choices=Education.choices,
        default=Education.Bachelors
    )
    industry = models.CharField(
        max_length=30,
        choices=Industry.choices,
        default=Industry.Business
    )
    experience = models.CharField(
        max_length=20,
        choices=Experience.choices,
        default=Experience.No_Experience
    )
    salary = models.IntegerField(default=1, validators=[
        MinValueValidator(1), MaxValueValidator(1000000)]
    )
    positon = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    # point = gismodels.PointField(default=Point(0.0, 0.0))
    lastDate = models.DateTimeField(default=return_date_time, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


# for Geometry map
# def save(self, *args, **kwargs):
#     print(os.environ('GEOC0DER_API'))
    
#     g = geocoder.mapquest(self.address, key=os.environ('GEOC0DER_API'))

#     print('show gmap :---------- ',g)

#     lng = g.lng
#     lat = g.lat

#     self.point = Point(lng, lat)
#     super(Job, self).save(*args, **kwargs)

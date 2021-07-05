from django.db import models
from django.http import request
from django.contrib.auth.models import User
# Create your models here.
class Portfolio(models.Model):
    username= models.OneToOneField(User, on_delete= models.CASCADE)
    name= models.CharField(max_length= 100)
    profile_image= models.ImageField(blank= True, null= True)
    mobile= models.CharField(max_length= 30)
    email= models.CharField(max_length= 100)
    date_of_birth= models.DateField()
    about_me= models.TextField()
    job_title= models.CharField(max_length= 100)
    title_description= models.TextField()
    age= models.IntegerField()
    degree= models.CharField(max_length= 100)
    instituion= models.CharField(max_length= 200)
    city= models.CharField(max_length= 100)
    home_address= models.CharField(max_length= 200)
    CHOICE= (
        ('O', 'O+'),
        ('A', 'A+'),
        ('B', 'B+'),
        ('A-', 'A-'),
        ('O-', 'O-'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB'),
    )
    blood_group= models.CharField(max_length=100, choices= CHOICE)
    freelancer= models.BooleanField(default= False)
    skills= models.CharField(max_length=100, default='')
    career_summary= models.TextField(default='')
    joining_date= models.DateField(null= True, blank= True)
    end_date= models.DateField(null= True, blank= True)
    company= models.CharField(max_length= 500, default='')
    # upload_cv= models.FileField()
    # portfoilo_image= models.ImageField()
    # portfoilo_link= models.CharField(max_length= 1000)
    # social_link= models.CharField(max_length= 1000)
    # map_link= models.CharField(max_length= 1000)
    services = models.CharField(max_length= 500, default='')
    pass_year= models.DateField(null= True, blank= True)
    
    
    def __str__(self):
        return f'{self.name} Profile' 
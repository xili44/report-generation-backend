from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

class Patient(models.Model):
    dob = models.DateField()
    dateOfOrder = models.DateField()
    dateOfReport = models.DateField()
    ethnicity = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    hn = models.CharField(validators=[RegexValidator(regex=r'^[0-9]{10}$', message='HN must contains 10 numbers exactly')], max_length=10)
    name = models.CharField(max_length=50)
    orderedBy = models.CharField(max_length=50)
    title = models.CharField(max_length=15)
    
class Genome(models.Model):
    CYP1A2  = models.BooleanField()  
    CYP2C19 = models.BooleanField()
    CYP2C9  = models.BooleanField()
    CYP2D6  = models.BooleanField()
    CYP3A4  = models.BooleanField()
    CYP3A5  = models.BooleanField()
    OPRM1   = models.BooleanField()
    SLCO1B1 = models.BooleanField()
    VKORC1  = models.BooleanField()
    
class Pharmacogenomics(models.Model):
    description = models.TextField()
    drug = models.CharField(max_length=50)
    gene = models.CharField(max_length=10)
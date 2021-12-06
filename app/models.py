from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_update = models.DateTimeField(auto_now_add=True)

class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to="app/img/candidate")

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name=models.CharField(max_length=150)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    logo_pic=models.ImageField(upload_to="app/img/company")

class JobDettails(models.Model):
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    jobname=models.CharField(max_length=250)
    companyname=models.CharField(max_length=250)
    companyaddress=models.CharField(max_length=250)
    jobdescription=models.CharField(max_length=250)
    qualification=models.CharField(max_length=500)
    responsiblity=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    companywebsite=models.CharField(max_length=250)
    companyemail=models.CharField(max_length=50)
    companycontact = models.CharField(max_length=20)
    salarypackage=models.CharField(max_length=250)
    experience=models.IntegerField()
    logo=models.ImageField(upload_to="app/img/jobpost",default="")


class AppltList(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    job = models.ForeignKey(JobDettails,on_delete=models.CASCADE)
    education = models.CharField(max_length=100)
    experience = models.IntegerField()
    website = models.CharField(max_length=100)
    min_salary = models.CharField(max_length=100)
    max_salary = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    resume = models.FileField(upload_to="app/resume")
    
        
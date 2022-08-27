from django.db import models

# Create your models here.

class facultyreg(models.Model):
    Staff_Id=models.CharField(max_length=100,null=True)
    Staff_Name=models.CharField(max_length=100,null=True)
    Address=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,null=True)
    Contact_No=models.IntegerField(null=True)
    Gender=models.CharField(max_length=100,null=True)
    DOB=models.DateField(null=True)
    Course=models.CharField(max_length=100,null=True)
    Semester=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)

class addStudent(models.Model):
    Register_No=models.CharField(max_length=100,null=True)
    Student_Name=models.CharField(max_length=100,null=True)
    Address=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,null=True)
    Contact_No=models.CharField(max_length=100,null=True)
    Gender=models.CharField(max_length=100,null=True)
    DOB=models.CharField(max_length=100,null=True)
    Course=models.CharField(max_length=100,null=True)
    Semester=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)


class materialup(models.Model):
    Semester=models.CharField(max_length=100,null=True)
    Subject=models.CharField(max_length=100,null=True)
    syllabus=models.FileField(upload_to='folder/',null=False)
    Study_Material=models.FileField(upload_to='folder/',null=False)
    Mock_Test=models.CharField(max_length=100,null=True)
    Project=models.CharField(max_length=100,null=True)

   
    

    

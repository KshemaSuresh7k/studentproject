from django import forms
from .models import  materialup
from .models import addStudent






class addStudentform(forms.ModelForm):
     class Meta:
        model=addStudent
        fields=('Register_No','Student_Name','Address','Email','Contact_No','Gender','Course','DOB','Semester','username','password')
        widgets={
             'Register_No':forms.TextInput(attrs={'class':'form-control'}),
             'Student_Name':forms.TextInput(attrs={'class':'form-control'}),
             'Address':forms.TextInput(attrs={'class':'form-control'}),
             'Email':forms.TextInput(attrs={'class':'form-control'}),
             'Contact_No':forms.TextInput(attrs={'class':'form-control'}),
             'Gender':forms.TextInput(attrs={'class':'form-control'}),
             'Course':forms.TextInput(attrs={'class':'form-control'}),
             'DOB':forms.TextInput(attrs={'class':'form-control'}),
            
             'Semester':forms.TextInput(attrs={'class':'form-control'}),
             'username':forms.TextInput(attrs={'class':'form-control'}),
             'password':forms.TextInput(attrs={'class':'form-control'}),


       }


class materialform(forms.ModelForm):
    class Meta:
        model=materialup
        fields=('Semester','Subject','syllabus','Study_Material','Mock_Test','Project')
        widgets={
            'Semester':forms.TextInput(attrs={'class':'form-control'}),
            'Subject':forms.TextInput(attrs={'class':'form-control'}),
            'syllabus':forms.TextInput(attrs={'class':'form-control'}),
            'Study_Material':forms.TextInput(attrs={'class':'form-control'}),
            'Mock_Test':forms.TextInput(attrs={'class':'form-control'}),
            'Project':forms.TextInput(attrs={'class':'form-control'}),
            
        }

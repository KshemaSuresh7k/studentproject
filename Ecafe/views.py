from django.shortcuts import redirect, render
from .models import addStudent, facultyreg, materialup
from .forms import addStudentform,materialform
from django.contrib.auth import logout


# Create your views here.


def studentadd(request):
     if request.method=="POST":
         Register_No=request.POST.get('Register_No')
         
         Student_Name=request.POST.get('Student_Name')
         Address=request.POST.get('Address')
         Email=request.POST.get('Email')
         Contact_No=request.POST.get('Contact_No')
         Gender=request.POST.get('Gender')
         Course=request.POST.get('Course')
         DOB=request.POST.get('DOB')
         
         Semester=request.POST.get('Semester')
         username=request.POST.get('username')
         password=request.POST.get('password')



         addStudent(Register_No=Register_No,Student_Name=Student_Name,Address=Address,Email=Email,Contact_No=Contact_No,Gender=Gender,DOB=DOB,Course=Course,Semester=Semester,username=username,password=password).save()
         
     return render(request,'studentadd.html')

def index(request):
    return render(request,'index.html')

def student(request):
    return render(request,'student.html')


def faculty(request):
    return render(request,'faculty.html')

def flog(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        cr=facultyreg.objects.filter(username=username,password=password)
        if cr:
            return redirect('folder')
        else:
           return render(request,'faculty.html')
    else:
        return render(request,'index.html')

def folder(request):
    if request.method=="POST":
         Register_No=request.POST.get('Register_No')
         
         Student_Name=request.POST.get('Student_Name')
         Address=request.POST.get('Address')
         Email=request.POST.get('Email')
         Contact_No=request.POST.get('Contact_No')
         Gender=request.POST.get('Gender')
         Course=request.POST.get('Course')
         DOB=request.POST.get('DOB')
         Semester=request.POST.get('Semester')
         username=request.POST.get('Username')
         password=request.POST.get('Password')
         addStudent(Register_No=Register_No,Student_Name=Student_Name,Address=Address,Email=Email,Contact_No=Contact_No,Gender=Gender,DOB=DOB,Course=Course,Semester=Semester,username=username,password=password).save()
        
    
    return render(request,'folder.html')


def material(request):
    if request.method=="POST":
        Semester=request.POST.get('Semester')
        Subject=request.POST.get('Subject')
        syllabus=request.POST.get('syllabus')
        Study_Material=request.POST.get('Study_Material')
        Mock_Test=request.POST.get('Mock_Test')
        Project=request.POST.get('Project')
        
        materialup(Semester=Semester,Subject=Subject,syllabus=syllabus,Study_Material=Study_Material,Mock_Test=Mock_Test,Project=Project).save()
    return render(request,'folder.html')


def welcomestudent(request):
    
    return render(request,'welcomestudent.html')

def student(request):
    return render(request,'student.html')   

def slog(request):
    if request.method=="POST":
        Student_Name = request.POST.get('Student_Name')
        Email = request.POST.get('Email')
        cr=addStudent.objects.filter( Student_Name= Student_Name,Email=Email)
        if cr:
            user_details=addStudent.objects.get(Student_Name= Student_Name,Email=Email)
            id=user_details.id
            Semester=user_details.Semester

            request.session['id']=id
            request.session['Semester']=Semester
            return redirect('welcomestudent')
        else:
           return render(request,'student.html')
    else:
        return render(request,'index.html')


def semester1(request):
    return render(request,'semester1.html')
#def semester2(request):
    #return render(request,'semester2.html')
def semester3(request):
    return render(request,'semester3.html')

def semester5(request):
    return render(request,'semester5.html')
def semester6(request):
    return render(request,'semester6.html')
def semester6(request):
    Semester=request.session['Semester']
    cr = materialup.objects.filter(Semester=Semester)
    return render(request,'semester6.html',{'cr':cr})

    


def sem2(request):
    Semester=request.session['Semester']
    cr = materialup.objects.filter(Semester=Semester)
    return render(request,'sem2.html',{'cr':cr})
def sem3(request):
    Semester=request.session['Semester']
    cr = materialup.objects.filter(Semester=Semester)
    return render(request,'sem3.html',{'cr':cr})

def sem4(request):
    Semester=request.session['Semester']
    cr = materialup.objects.filter(Semester=Semester)
    return render(request,'sem4.html',{'cr':cr})

def sem5(request):
    Semester=request.session['Semester']
    cr = materialup.objects.filter(Semester=Semester)
    return render(request,'sem5.html',{'cr':cr})
def sem6(request):
    Semester=request.session['Semester']
    cr = materialup.objects.filter(Semester=Semester)
    return render(request,'sem6.html',{'cr':cr})

    

def logoutuser(request):
    logout(request)
    return redirect('index')
def view1(request):
    # cr=addStudent.objects.filter( Student_Name= Student_Name,Email=Email)
    cr=materialup.objects.get()
    return render(request,"A01.html",{'cr':cr})

def sem2(request):
    Semester=request.session['Semester']
    cr = materialup.objects.filter(Semester=Semester)
    return render(request,'sem2.html',{'cr':cr})

def sem1(request):
    Semester=request.session['Semester']
    cr = materialup.objects.filter(Semester=Semester)
    return render(request,'sem1.html',{'cr':cr})


def semester2(request):
    Semester=request.session['Semester']
    cr = materialup.objects.filter(Semester=Semester)
    return render(request,'semester2.html',{'cr':cr})
#def semester2(request):
    #return render(request,'semester2.html')

def semester1(request):
    Semester=request.session['Semester']
    cr = materialup.objects.filter(Semester=Semester)
    return render(request,'semester1.html',{'cr':cr})

def semester4(request):
    Semester=request.session['Semester']
    cr = materialup.objects.filter(Semester=Semester)
    return render(request,'semester4.html',{'cr':cr})


def viewsem1(request):
    Semester=request.session['Semester']
    cr = materialup.objects.filter(Semester=Semester)
    return render(request,'viewsem1.html')




def A01(request):
    Semester=request.session['Semester']
    cr=materialup.objects.filter(Semester=Semester)

    # print(cr)
    # if cr:
    #  return render(request,"A01.html",{'cr':cr})
    return render(request,'A01.html',{'cr':cr})
def viewsyllabus(request):
    # cr=addStudent.objects.filter( Student_Name= Student_Name,Email=Email)
    cr=materialup.objects.all()
    return render(request,"viewsyllabus.html",{'cr':cr})



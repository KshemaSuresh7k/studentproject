#from django.shortcuts import render
from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    path('student/',views.student,name='student'),
    path('faculty/',views.faculty,name="faculty"),
    path('slog/',views.slog,name="slog"),
    path('flog/',views.flog,name="flog"),
    path('material/',views.material,name='material'),
    path('folder/',views.folder,name='folder'),
    path('welcomestudent/',views.welcomestudent,name='welcomestudent'),
    path('studentadd/',views.studentadd,name='studentadd'),
    path('semester1/',views.semester1,name='semester1'),
    path('semester2/',views.semester2,name='semester2'),
    path('semester3/',views.semester3,name='semester3'),
    path('semester4/',views.semester4,name='semester4'),
    path('semester5/',views.semester5,name='semester5'),
    path('semester6/',views.semester6,name='semester6'),
    path('A01/',views.A01,name='A01'),
    path('viewsem1/',views.viewsem1,name='viewsem1'),

    path('sem1/',views.sem1,name='sem1'),
    path('sem2/',views.sem2,name='sem2'),
    path('sem3/',views.sem3,name='sem3'),
    path('sem4/',views.sem4,name='sem4'),
    path('sem5/',views.sem5,name='sem5'),
    path('sem6/',views.sem6,name='sem6'),
    
    path('logoutuser/',views.logoutuser,name='logoutuser'), 
    path('view1/',views.view1,name='view1'),
    path('viewsyllabus/',views.viewsyllabus,name='viewsyllabus'),
]



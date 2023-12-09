from django.shortcuts import render, redirect
from .models import Course

def course_list(request):
    courses = Course.objects.all() 
    context = {'courses': courses} 
    return render(request, 'courses/course_list.html', context) 

def course_add(request):
    if request.method == 'POST': # if the request is a POST request
        course_id = request.POST['course_id'] 
        course_title = request.POST['course_title'] 
        instructor = request.POST['instructor'] 
        course = Course(course_id=course_id, course_title=course_title, instructor=instructor)
        course.save() # save the Course object to the database
        return redirect('course_list') 
    else: # if the request is a GET request
        return render(request, 'courses/course_add.html')



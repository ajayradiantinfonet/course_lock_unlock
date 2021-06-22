from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    value_course=Course.objects.values('cat')
    sun=[]
    for val in value_course:
            sun.append(val['cat'])
    res=[]
    sun=set(sun)
    # sun=list(sun1)
    for x in sun:
        course_content =Course.objects.filter(cat=x)
        res.append(course_content)
    return render(request,'list.html',{'res':res})

def premimum(request,id):
    course_content = Course.objects.get(id=id)
    return render(request,'premimum.html',{'course_content':course_content})
from django.shortcuts import get_object_or_404, render

from student.models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    for student in students:
        print("url:"+ student.pic.url)
    return render(request, 'students/index.html', context={"students":students})

def detail(request, slug):
    student = get_object_or_404(Student, slug = slug)
    return render(request, 'students/detail.html', context={"student": student})
  
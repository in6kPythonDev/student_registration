from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from student_registration.settings import LANGUAGES
from student_registration.student_form.forms import StudentForm
from student_registration.student_form.models import Student

def show_students(request):
    students = Student.objects.all()
    return render_to_response('show_students.html', {'students' : students})


@csrf_exempt
def edit(request, student_id=None):
    languages = LANGUAGES

    if student_id is None:
        student = Student()
    else:
        student = get_object_or_404(Student, id=student_id)

    if request.POST:
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student_registration/show_students')
    else:
        form = StudentForm(instance=student)

    return render_to_response('student_form.html', { 'form': form, 'languages': languages })
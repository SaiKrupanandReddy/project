from django.views.generic import TemplateView, CreateView, ListView, DeleteView, DetailView
from accounts.ptest import StudentTestMixin
from django import views
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from accounts.models import Classroom,Teacher,User,Section, Resource,Assignment,AssignmentSubmission
from django.http import HttpResponse
from .forms import AssignmentSubmissionForm, JoinClassroomForm
from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.


def student_ta(request):
    return HttpResponse("Student's Dashboard")
    
class StudentDashBoard(StudentTestMixin, TemplateView):
    template_name = "students/dashboard.html"

def ViewClassRoomDetail(request,code):
    return_context = {}
    return_context['classroom'] = get_object_or_404(Classroom, code=code)
    return render(request, 'students/classroom_detail.html', context=return_context)

def viewResources(request, pk):
    res_dict = {}
    res_dict['section'] = get_object_or_404(Section, pk=pk)
    return render(request, 'students/resources.html', context=res_dict)

def viewAssign(request, pk):
    res_dict = {}
    res_dict['section'] = get_object_or_404(Section, pk=pk)
    return render(request, 'students/assignments.html', context=res_dict)

def ViewAllClassrooms(request):
    res_dict = {}
    res_dict['classrooms'] = Classroom.objects.all()
    return render(request, 'students/all_classrooms.html', context=res_dict)

class AssignmentSubmissionCreate(CreateView, SuccessMessageMixin):
    model = AssignmentSubmission
    form_class = AssignmentSubmissionForm
    template_name = "students/assignmentsubmission.html"
    success_message ="Assignment Submited well"
    def form_valid(self, form):
        form.instance.assignment = get_object_or_404(Assignment, pk=self.kwargs['pk'])
        form.instance.student = self.request.user.students
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('students:assignments', kwargs={'pk':Assignment.objects.get(pk=self.kwargs['pk']).section.pk})

def viewStudentAssignment(request, pk):
    res_dict = {}
    student_obj = request.user.students
    assignment_obj = Assignment.objects.get(pk=pk)

    if AssignmentSubmission.objects.filter(assignment=assignment_obj).filter(student=student_obj).exists():
        res_dict['assignment'] = assignment_obj
        res_dict['submission'] = AssignmentSubmission.objects.filter(assignment=assignment_obj).filter(student=student_obj)[0]
        res_dict['assignmentfilename'] = res_dict['submission'].file.name.split('/')[-1]
        return render(request, template_name='students/my_assignment.html', context=res_dict)
    else:
        return redirect('students:submit_assignment', pk=pk)

class DeleteAssignmentSubmission(DeleteView):
    model = AssignmentSubmission
    template_name = "students/deletesubmission.html"
    success_message ="Assignment Deleted well"

    def get_success_url(self):
        return reverse('students:assignments', kwargs={'pk':self.object.assignment.section.pk})

def joinAClassroom(request):
    joinForm = JoinClassroomForm()

    if request.method == 'POST':
        joinForm = JoinClassroomForm(request.POST)
        if joinForm.is_valid():
            code = joinForm.cleaned_data['code']
            if Classroom.objects.filter(code=code).exists():
                print('Coide Exists', joinForm.cleaned_data['code'])

                if request.user.students.classrooms.filter(code=code).exists():
                    # messages.success(request, 'You Already A member')
                    print('You Already A member')
                    return HttpResponseRedirect(reverse('students:dashboard'))
                else:
                    messages.success(request, 'You are not a member, Joiniung you soon..')
                    print('You are not a member, Joiniung you soon..')
                    request.user.students.classrooms.add(Classroom.objects.filter(code=code).first())
                    messages.success(request, 'You have Joined to the classroom!')
                    print('You have Joined to the classroom!')
                    return HttpResponseRedirect(reverse('students:dashboard'))
            else:
                messages.error(request, 'No Such code found in our databases')
                print('No Such code found in our databases')
    return render(request, 'students/join_classroom.html', {'form':joinForm})


def LeaveAClassroom(request,code):
    request.user.students.classrooms.remove(Classroom.objects.filter(code=code).first())
    print(f"You have successfull leaved the class with code {code}")
    messages.info(request, f"You have successfull leaved the class with code {code}")
    return HttpResponseRedirect(reverse('students:dashboard'))

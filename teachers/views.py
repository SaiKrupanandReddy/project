from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, DetailView
from accounts.models import Classroom,Teacher,User,Section, Resource,Assignment,AssignmentSubmission
from .forms import ClassroomForm, SectionForm,ResourceForm, AssignmentForm
from accounts.ptest import StudentTestMixin, TeacherTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse


# Create your views here.



def index_ta(request):
    return HttpResponse("Teacher's Dashboard")

class ViewDash(TeacherTestMixin,TemplateView):
    template_name = "teachers/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classrooms'] = self.request.user.teachers.classrooms.all()
        return context


def add_classroom(request):
    form = ClassroomForm()

    def form_valid(self, form):
        classroom = form.save(commit=False)
        classroom.teacher = Teacher.objects.get(user=self.request.user.teachers)
        messages.add(self.request, "A classroom Has been Added!")
        classroom.save()
        return HttpResponseRedirect(self.get_success_url())

class CreateClassRoom(CreateView, SuccessMessageMixin):
    model = Classroom
    success_message ="Class updated well"
    form_class = ClassroomForm
    template_name = "teachers/addclassroom.html"

    def form_valid(self, form):
        form.instance.teacher = self.request.user.teachers
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('teachers:dashboard')

class DeleteClassRoom(DeleteView):
    model = Classroom
    template_name = "teachers/deleteclassroom.html"

    # Should match the value after ':' from url <slug:the_slug>
    slug_url_kwarg = 'code'

    # Should match the name of the slug field on the model
    slug_field = 'code' # DetailView's default value: optional

    def get_success_url(self):
        return reverse('teachers:dashboard')

def DetailClassroom(request,code):
    context_dict = {}
    room = get_object_or_404(Classroom, code=code)
    context_dict['classroom'] = room
    return render(request, 'teachers/classroom_detail.html', context=context_dict)

class CreateSection(CreateView):
    model = Section
    form_class = SectionForm
    template_name = "teachers/add_section.html"

    def form_valid(self, form):
        form.instance.classroom = get_object_or_404(Classroom, code=self.kwargs['code'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('teachers:classroom_detail', kwargs={'code':self.kwargs['code']})

class DeleteSection(DeleteView):
    model = Section
    template_name = "teachers/delete_section.html"

    def get_success_url(self):
        return reverse('teachers:classroom_detail', kwargs={'code':self.object.classroom.code})

def ViewResources(request, pk):
    context_dict = {}
    section = get_object_or_404(Section, pk=pk)
    print(section)
    context_dict['section'] = section
    return render(request, 'teachers/resources.html', context=context_dict)

class CreateResources(CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = "teachers/add_resource.html"

    def form_valid(self, form):
        form.instance.section = get_object_or_404(Section, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('teachers:resources', kwargs={'pk':self.kwargs['pk']})

class DeleteResources(DeleteView):
    model = Resource
    template_name = "teachers/delete_resource.html"

    def get_success_url(self):
        return reverse('teachers:resources', kwargs={'pk':self.object.section.pk})


def ViewAssignment(request, pk):
    context_dict = {}
    section = get_object_or_404(Section, pk=pk)
    print(section)
    context_dict['section'] = section
    return render(request, 'teachers/assignments.html', context=context_dict)


class CreateAssignment(CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = "teachers/add_assignment.html"

    def form_valid(self, form):
        form.instance.section = get_object_or_404(Section, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('teachers:assignments', kwargs={'pk':self.kwargs['pk']})

class DeleteAssignment(DeleteView):
    model = Assignment
    template_name = "teachers/delete_assignment.html"

    def get_success_url(self):
        return reverse('teachers:assignments', kwargs={'pk':self.object.section.pk})

def SubmitAssignment(request,pk):
    context_dict = {}
    assignment = Assignment.objects.get(pk=pk)

    context_dict['assignment'] = assignment
    context_dict['assignment_submissions'] = AssignmentSubmission.objects.filter(assignment=assignment)

    return render(request, template_name='teachers/submissions.html', context=context_dict)

def StudentClassroom(request,code):
    print("already in this view")
    context_dict = {}
    classroom = get_object_or_404(Classroom, code=code)

    context_dict['classroom'] = classroom
    context_dict['classroom_students'] = classroom.students.all()

    print(context_dict)
    return render(request, template_name='teachers/classroomstudents.html', context=context_dict)

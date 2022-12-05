from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from django.urls import reverse
from django.utils import timezone, text
from django.core.validators import MaxValueValidator, MinValueValidator
import os
import datetime
import random
import string



_ = lambda x: x


def string_generator(size=8, char_choices=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(char_choices) for _ in range(size))



class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)


class Stream(models.Model):
    name = models.CharField(_("Stream Name"),max_length=250,blank=False,unique=True)
    class Meta:
        db_table = 'stream_table'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("stream_info", kwargs={"pk": self.pk})


class Class(models.Model):
    stream = models.ForeignKey("Stream",on_delete=models.CASCADE,related_name="classes",blank=False)
    year = models.PositiveIntegerField(blank=False,default=2022,validators=[MaxValueValidator(2030),MinValueValidator(2022)])
    name = models.CharField(_("student_class"),max_length=250,blank=False,unique=True)
    semester = models.PositiveIntegerField(blank=False,default=1,validators=[MaxValueValidator(8),MinValueValidator(1)])
    class Meta:
        db_table ='class_table'
    def __str__(self):
        return f"Classs {self.name} Sem:{self.semester}"
    def get_absolute_url(self):
        return reverse("class_info", kwargs={"pk": self.pk})


class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='teachers')
    stream = models.ForeignKey("Stream",on_delete=models.CASCADE,related_name="teachers",blank=False)
    class Meta:
        db_table ="teachers_table"
    def __str__(self):
        return f"Teacher: {self.user.username}"
    def get_absolute_url(self):
        return reverse("teacher_detail", kwargs={"pk": self.pk})




class Classroom(models.Model):
    teacher = models.ForeignKey("Teacher",on_delete=models.CASCADE,blank=False,related_name='classrooms')
    subject = models.CharField(_("Unit Name"),max_length=50,blank=False)
    code = models.SlugField(_("Unit Code"),max_length=10,default=string_generator,unique=True)
    semester = models.PositiveIntegerField(blank=False,default=1,validators=[MaxValueValidator(8),MinValueValidator(1)])
    created_timestamp = models.DateTimeField(default=timezone.now,editable=False)
    class Meta:
        db_table ="classroom_table"
    def __str__(self):
        return self.code
    def get_absolute_url(self):
        return reverse("Classroom_info", kwargs={"pk": self.pk})


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='students')
    current_class = models.ForeignKey("Class",verbose_name=_("Class"),on_delete=models.CASCADE,blank=False,related_name='students')
    roll_no = models.PositiveIntegerField(_("Roll No."),blank=False)
    student_id = models.CharField(_("Student ID"),max_length=50,blank=False,unique=True)
    classrooms = models.ManyToManyField("Classroom", related_name='students', blank=True)

    class Meta:
        db_table ="student_table"
        unique_together = ('roll_no', 'current_class')
    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse("student_info", kwargs={"pk": self.pk})


class Section(models.Model):
    classroom = models.ForeignKey("Classroom",on_delete=models.CASCADE,blank=False,related_name='sections')
    title = models.CharField(_("section title"),max_length=150)
    created_timestamp = models.DateTimeField(default=timezone.now,editable=False)
    class Meta:
        db_table ="section_break_table"
    def __str__(self):
        return f'{self.title}: {self.classroom.subject}'
    def get_absolute_url(self):
        return reverse("section_info", kwargs={"pk": self.pk})



class Resource(models.Model):
    title = models.CharField(_("resource title"),max_length=150)
    text = models.TextField()
    created_timestamp = models.DateTimeField(default=timezone.now,editable=False)
    section = models.ForeignKey("Section",on_delete=models.CASCADE,related_name='resources',blank=False)
    file = models.FileField(upload_to="files/resources/",blank=True,max_length=999)
    class Meta:
        db_table = "resources_table"
    def __str__(self):
        return f"Title: {self.title}"
    def get_absolute_url(self):
        return reverse("resource_info", kwargs={"pk": self.pk})



class Assignment(models.Model):
    title = models.CharField(_("section title"),max_length=150)
    section = models.ForeignKey("Section",on_delete=models.CASCADE,related_name='assignments',blank=False)
    text = models.TextField()
    created_timestamp = models.DateTimeField(default=timezone.now,editable=False)
    deadline = models.DateTimeField(default=timezone.now,blank=False)
    file = models.FileField(upload_to="files/assignments/",blank=True,max_length=999)
    class Meta:
        db_table ="assignment_table"
    def __str__(self):
        return f"Assignment : {self.title} Deadline {self.deadline}"

    def get_absolute_url(self):
        return reverse("assignment_detail", kwargs={"pk": self.pk})



class AssignmentSubmission(models.Model):
    student = models.ForeignKey("Student",verbose_name=_("student submited"),on_delete=models.CASCADE,related_name='assignment_submissions',blank=False)
    assignment = models.ForeignKey("Assignment",on_delete=models.CASCADE,related_name='assignment_submissions',blank=False)
    file = models.FileField(upload_to="files/submissions/",blank=False,max_length=999)
    submission_timestamp = models.DateTimeField(default=timezone.now,editable=False)
    class Meta:
        db_table ="submission_table"
        unique_together = ('student', 'assignment')
    def __str__(self):
        return f'Submission :{self.assignment} By {self.student}'
    def get_absolute_url(self):
        return reverse("submission_info", kwargs={"pk": self.pk})





# TEST CASES for login.
# ERROR cases Sequence.

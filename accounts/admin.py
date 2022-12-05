from django.contrib import admin

# Register your models here.

from . import models
admin.site.register(models.User)
admin.site.register(models.Stream)
admin.site.register(models.Class)
admin.site.register(models.Teacher)
admin.site.register(models.Classroom)
admin.site.register(models.Student)
admin.site.register(models.Section)
admin.site.register(models.Resource)
admin.site.register(models.Assignment)
admin.site.register(models.AssignmentSubmission)

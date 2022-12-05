from django.urls import path, include
from . import views


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'accounts'



urlpatterns = [
    path("", views.index, name='home'),


    path("account", views.entry, name='signup'),
    path('login', LoginView.as_view(template_name='accounts/login.html',redirect_authenticated_user=True), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    #teacger
    path('signup/teacher/<int:stream_pk>', views.CreateTeacher.as_view(), name='teacher_signup'),
    path('signup/teacher/stream', views.AddCourse.as_view(template_name = "accounts/teachers/stream.html"), name='teacher_stream'),

    #student
    path('signup/student/stream', views.AddCourse.as_view(template_name = "accounts/students/stream.html"), name='student_stream'),
    path('signup/student/<int:stream_pk>', views.CreateStudent.as_view(), name='student_signup'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

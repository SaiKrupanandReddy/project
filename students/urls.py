from django.urls import include, path
from . import views

app_name = 'students'

urlpatterns = [
    # path("", views.student_ta, nsame='dashboard'),
    path('', views.StudentDashBoard.as_view(), name='dashboard'),
    path('section/<int:pk>/assignments/', views.viewAssign, name='assignments'),
    path('delete-submission/<int:pk>/', views.DeleteAssignmentSubmission.as_view(), name='delete_submission'),
    path('assignment/<int:pk>/', views.viewStudentAssignment, name='my_assignment'),
    path('classroom/<slug:code>/', views.ViewClassRoomDetail,name='classroom_detail'),
    path('join-new/',views.joinAClassroom, name='join_classroom'),
    path('all_classes',views.ViewAllClassrooms, name='all_classroom'),
    path('section/<int:pk>/resources/', views.viewResources, name='resources'),
    path('assignment/<int:pk>/submit/', views.AssignmentSubmissionCreate.as_view(), name='submit_assignment'),
    path('leave-classroom/<slug:code>/', views.LeaveAClassroom,name='leave_classroom'),
]

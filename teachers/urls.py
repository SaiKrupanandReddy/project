from django.urls import include, path
from . import views

app_name = 'teachers'

urlpatterns = [
    # path("", views.index_ta, name='dashboard')
    path('', views.ViewDash.as_view(),name='dashboard'),
    path('classroom/add/', views.CreateClassRoom.as_view(),  name='add_classroom'),
    path('classroom/<slug:code>/delete/', views.DeleteClassRoom.as_view(),  name='delete_classroom'),
    path('classroom/<slug:code>/',views.DetailClassroom, name='classroom_detail'),
    path('resources/<int:pk>/add/',views.CreateResources.as_view(), name='add_resource'),
    path('resources/delete/<int:pk>/', views.DeleteResources.as_view(), name='delete_resource'),
    path('assignments/<int:pk>/',views.ViewAssignment, name='assignments'),
    path('assignments/<int:pk>/add/',views.CreateAssignment.as_view(), name='add_assignment'),
    path('assignments/delete/<int:pk>/',views.DeleteAssignment.as_view(), name='delete_assignment'),
    path('classroom/<slug:code>/add/', views.CreateSection.as_view(),  name='add_section'),
    path('submissions/<int:pk>/', views.SubmitAssignment, name='assignment_submissions'),
    path('classroom/students/<str:code>/', views.StudentClassroom, name='classroom_students'),
    path('section/<int:pk>/delete/', views.DeleteSection.as_view(), name='delete_section'),
    path('resources/<int:pk>/', views.ViewResources,  name='resources'),
]

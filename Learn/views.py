from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
@login_required
def Dash(request):
    print("We here")
    if request.user.is_student:
        return redirect('students:dashboard')
    if request.user.is_teacher:
        return redirect('teachers:dashboard')
    if request.user.is_superuser:
        return redirect('admin:index')

from myapp.views.is_user_admin_view import is_user_admin
from .login_required_decorator import login_required
from django.shortcuts import render

from ..models.machine import Machine


@login_required
def get_machines(request):
    is_admin = is_user_admin(request)
    return render(request, 'machines.html', context={'machines': Machine.objects.all(), 'is_admin': is_admin})


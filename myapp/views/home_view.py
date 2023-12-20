from .is_user_admin_view import is_user_admin
from .login_required_decorator import login_required
from django.shortcuts import render

@login_required
def home(request):
    is_admin = is_user_admin(request)
    context = {
        'user_name': request.user.name,
        'is_admin': is_admin,
    }
    return render(request, 'index.html', context=context)
from myapp.models.user import CustomUser
from myapp.views.is_user_admin_view import is_user_admin
from django.shortcuts import render
from .login_required_decorator import login_required


@login_required
def get_users(request):
    is_admin = is_user_admin(request)
    if not is_admin:
        return render(request, 'users.html', context={'is_admin': is_admin})

    users = CustomUser.objects.all()
    user_datas = []
    for user in users:
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'is_staff': user.is_staff,
            'is_admin': user.is_admin,
        }
        user_datas.append(user_data)
    context = {
        'user_datas': user_datas,
        'is_admin': is_admin
    }

    return render(request, 'users.html', context=context)
from django.shortcuts import redirect
from django.shortcuts import render
from myapp.models.user import CustomUser
from myapp.views.is_user_admin_view import is_user_admin
from .login_required_decorator import login_required

@login_required
def user_register(request):
    is_admin = is_user_admin(request)
    if request.method == 'POST':
        post = request.POST
        print(post.__dict__)
        user = CustomUser.objects.create_user(
            email=post.get('email'),
            password=post.get('password1'),
            first_name=post.get('first_name'),
            last_name=post.get('last_name'),
            is_staff=True if post.get('is_staff') == 'on' else False,
            is_admin=True if post.get('is_admin') == 'on' else False
        )
        return redirect("userstable")

    return render(request, 'register.html', context={'is_admin': is_admin})

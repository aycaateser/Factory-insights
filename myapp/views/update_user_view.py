from django.shortcuts import redirect
from .login_required_decorator import login_required
from myapp.models.user import CustomUser
from myapp.views.is_user_admin_view import is_user_admin
from django.shortcuts import render

@login_required
def update_user(request, user_id):
    is_admin = is_user_admin(request)
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return render(request, 'update_user.html', context={
            'user': None, 'is_admin': is_admin, 'error_message': 'User not found'})

    if request.method == 'POST':
        post = request.POST


        # Update the user fields
        user.email = post.get('email')
        user.first_name = post.get('first_name')
        user.last_name = post.get('last_name')
        user.is_staff = True if post.get('is_staff') == 'on' else False
        user.is_admin = True if post.get('is_admin') == 'on' else False

        # Save the updated user
        user.save()

        return redirect("userstable")

    return render(request, 'update_user.html', context={'user': user, 'is_admin': is_admin})


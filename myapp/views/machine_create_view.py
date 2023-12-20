from django.shortcuts import render, redirect
from .login_required_decorator import login_required
from myapp.models.machine import Machine
from myapp.views.is_user_admin_view import is_user_admin


@login_required
def machine_create(request):
    is_admin = is_user_admin(request)
    if request.method == 'POST':
        post = request.POST
        Machine.objects.create(
            name=post.get('machine_name'),
            brand=post.get('brand_name'),
            is_active=bool(post.get('is_active'))
        )

        return redirect("machines")

    return render(request, 'machine_create.html', context={'is_admin': is_admin})

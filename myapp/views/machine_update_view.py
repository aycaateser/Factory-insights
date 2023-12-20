from django.shortcuts import redirect
from django.shortcuts import render
from myapp.models.machine import Machine
from myapp.views.is_user_admin_view import is_user_admin
from .login_required_decorator import login_required

@login_required
def machine_update(request, machine_id):
    is_admin = is_user_admin(request)

    try:
        machine = Machine.objects.get(id=machine_id)
    except Machine.DoesNotExist:
        return render(request, 'machine_update.html', context={'machine': None, 'is_admin': is_admin,
                                                               'error_message': 'Machine not found'})

    if request.method == 'POST':
        post = request.POST

        machine.name = post.get('machine_name')
        machine.brand = post.get('brand_name')
        machine.is_active = bool(post.get('is_active'))

        machine.save()

        return redirect("machines")

    return render(request, 'machine_update.html', context={'machine': machine, 'is_admin': is_admin})

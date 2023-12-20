from django.shortcuts import redirect
from myapp.models.machine import Machine
from myapp.models.user import CustomUser
from myapp.views.is_user_admin_view import is_user_admin
from .login_required_decorator import login_required
from myapp.models.factory import Factory
from django.shortcuts import render
from .login_required_decorator import login_required

@login_required
def factory_update(request, factory_id):
    is_admin = is_user_admin(request)
    try:
        factory = Factory.objects.get(pk=factory_id)
    except Factory.DoesNotExist:
        return render(request, 'factory_update.html', context={'factory': None, 'is_admin': is_admin,
                                                               'error_message': 'Factory not found'})


    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        product = request.POST.get('product')
        employees_ids = request.POST.getlist('employees')
        machines_ids = request.POST.getlist('machines')
        is_active = bool(request.POST.get('is_active'))

        employees = CustomUser.objects.filter(id__in=employees_ids)
        machines = Machine.objects.filter(id__in=machines_ids)

        factory.name = name
        factory.address = address
        factory.product = product
        factory.is_active = is_active

        factory.employees.set(employees)
        factory.machines.set(machines)

        factory.save()

        return redirect("factories")

    context = {
        'factory': factory,
        'users': CustomUser.objects.all(),
        'machines': Machine.objects.all(),
        'is_admin': is_admin,
    }

    return render(request, 'factory_update.html', context=context)

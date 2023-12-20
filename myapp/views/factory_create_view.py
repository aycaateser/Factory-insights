from django.shortcuts import redirect
from django.shortcuts import render
from .is_user_admin_view import is_user_admin
from .login_required_decorator import login_required
from ..models.machine import Machine
from ..models.user import CustomUser
from ..models.factory import Factory

@login_required
def factory_create(request):
    is_admin = is_user_admin(request)
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        product = request.POST.get('product')
        employees_ids = request.POST.getlist('employees')
        machines_ids = request.POST.getlist('machines')
        is_active = bool(request.POST.get('is_active'))

        employees = CustomUser.objects.filter(id__in=employees_ids)
        machines = Machine.objects.filter(id__in=machines_ids)

        factory = Factory.objects.create(
            name=name,
            address=address,
            product=product,
            is_active=is_active
        )

        factory.employees.set(employees)
        factory.machines.set(machines)

        return redirect("factories")

    context = {
        'users': CustomUser.objects.all(),
        'machines': Machine.objects.all(),
        'is_admin': is_admin,
    }

    return render(request, 'factory_create.html', context=context)

from myapp.views.get_user_factories_view import get_user_factories
from myapp.views.is_user_admin_view import is_user_admin
from django.shortcuts import render
from .login_required_decorator import login_required
from ..models.factory import Factory

@login_required
def get_factories(request):
    factory_datas = []
    is_admin = is_user_admin(request)
    if is_admin:
        factories = Factory.objects.all()
    else:
        factories = get_user_factories(request.user)

    for factory in factories:
        employees = [employee.name for employee in factory.employees.all()]
        machines = [machine.name for machine in factory.machines.all()]
        factory_data = {
            'id': factory.id,
            'name': factory.name,
            'address': factory.address,
            'product': factory.product,
            'employees': employees,
            'machines': machines,
        }
        factory_datas.append(factory_data)

    return render(request, 'factories.html', context={'factories': factory_datas, 'is_admin': is_admin})

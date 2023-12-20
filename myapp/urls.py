from django.contrib import admin
from django.urls import path, include

from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('user-register/', views.user_register, name='user_register'),
    path('login/', views.login, name='login'),
    path('userstable/', views.get_users, name='userstable'),
    path('user-update/<user_id>', views.update_user, name='update_user'),
    path('register-user/', views.user_register, name='register_user'),
    path('factories/', views.get_factories, name='factories'),
    path('factory-create/', views.factory_create_view.factory_create, name='factory_create'),
    path('update-factory/<factory_id>', views.factory_update, name='factory_update'),
    path('machines/', views.get_machines, name='machines'),
    path('machine-create/', views.machine_create, name='machine_create'),
    path('update-machine/<machine_id>', views.machine_update, name='update_machine'),
    path('logout/', views.logout_view, name='logout'),
]


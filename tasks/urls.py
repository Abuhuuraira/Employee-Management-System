from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("employees/", views.employee_list, name="employee_list"),
    path("tasks/", views.task_list, name="task_list"),
    path("departments/", views.department_list, name="department_list"),
    path("login/", views.login_view, name="login"),
]

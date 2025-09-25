from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

from django.shortcuts import render

def dashboard(request):
    return render(request, "dashboard.html")

def employee_list(request):
    return render(request, "tasks/employee_list.html")

def task_list(request):
    return render(request, "tasks/task_list.html")

def department_list(request):
    return render(request, "tasks/department_list.html")

def login_view(request):
    return render(request, "tasks/login.html")



# GET (list user's tasks) + POST (create new task for logged-in user)
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # only return tasks of the logged-in user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # set the user automatically
        serializer.save(user=self.request.user)


# GET (single), PUT/PATCH (update), DELETE (remove)
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # user can only access their own tasks
        return Task.objects.filter(user=self.request.user)

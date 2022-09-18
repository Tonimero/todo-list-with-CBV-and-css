from django.urls import path

from todo_app.views import TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='index')
]

from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from task_app.models import Task
from task_app.serializers import TaskSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def createTask(request):
    task_data = JSONParser().parse(request)
    tasks_serializer = TaskSerializer(data=task_data)
    if tasks_serializer.is_valid():
        tasks_serializer.save()
        return JsonResponse(tasks_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(tasks_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fetchTasks(request):
    task = Task.objects.all()
    tasks_serializer = TaskSerializer(task, many=True)
    return JsonResponse(tasks_serializer.data, safe=False)
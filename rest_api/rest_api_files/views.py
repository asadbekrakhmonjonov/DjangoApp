from django.shortcuts import render, redirect
from .models import Task
from rest_framework.views import APIView
from . serializers import TaskSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


from .serializers import *
# Create your views here.
class apiOverview(APIView):
    def get(self, request):
        api_urls = {
            'List': '/task-list',
            'Detail View': '/task-detail/str:pk>/',
            'Create View': '/task-create/',
            'Update': '/task-update/str:pk>/',
            'Delete': '/task-delete/str:pk>/',
        }
        return Response(api_urls)
class taskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
class taskDetail(APIView):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)
class taskCreate(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
class taskUpdate(APIView):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)
    def put(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
class taskDelete(APIView):
    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return Response('user was deleted')









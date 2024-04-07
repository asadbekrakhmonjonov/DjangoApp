from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
urlpatterns = [
    path('', views.apiOverview.as_view()),
    path('task-list/', views.taskList.as_view(),name='task-list'),
    path('task-detail/<str:pk>/', views.taskDetail.as_view(), name='task-detail'),
    path('task-create/', views.taskCreate.as_view(),name='task_create'),
    path('task-update/<str:pk>/', views.taskUpdate.as_view(),name='task_update'),
    path('task-delete/<str:pk>/', views.taskDelete.as_view(),name='task_delete'),

]
from django.urls import path
from .import views
urlpatterns = [
    path('', views.MainPage.as_view()),
    path('users/', views.UserList.as_view()),
    path('books/', views.BookList.as_view()),

]
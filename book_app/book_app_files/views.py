from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Book  # Import your models here
from .serializers import UserSerializer, BookSerializer  # Import your serializers here

class MainPage(APIView):
    def get(self,request):
        api_urls = {
            'Users': 'users',
            'Books': 'books',

        }
        return Response(api_urls)
class UserList(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)  # Return error response with status code 500 if any exception occurs
    def post(self, request):

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
    def put(self, request, pk):

        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class BookList(APIView):
    def get(self, request):

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)
    def post(self, request):

        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def put (self, request, pk):

        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


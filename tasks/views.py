from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Task
from .serializers import TaskSerializer
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions, viewsets, status
from .serializers import TaskSerializer
from .permissions import IsOwner

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]#

    def get(self, request):
        tasks = Task.objects.filter(owner=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.status == 'completed':
            return Response({'detail': 'Cannot edit a completed task.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)


class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, owner=request.user)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk, owner=request.user)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk, owner=request.user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskMarkCompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, owner=request.user)
        if task.status != 'completed':
            task.status = 'completed'
            task.completed_at = timezone.now()
            task.save()
            return Response({'status': 'Task marked as complete'}, status=status.HTTP_200_OK)
        return Response({'error': 'Task is already completed'}, status=status.HTTP_400_BAD_REQUEST)

class TaskMarkIncompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, owner=request.user)
        if task.status == 'completed':
            task.status = 'pending'
            task.completed_at = None
            task.save()
            return Response({'status': 'Task marked as incomplete'}, status=status.HTTP_200_OK)
        return Response({'error': 'Task is not completed'}, status=status.HTTP_400_BAD_REQUEST)


#2. User List Endpoint (Optional, Superuser Only)
#Create a view to test the superuser's ability to manage users:


from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

class DebugAPIView(APIView):
    def get(self, request):
        print(request.headers)
        return Response({"message": "Debugging"})
    

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
from django.utils.decorators import method_decorator


@csrf_exempt
def my_view(request):
    pass
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], url_path='register', permission_classes=[])
    def register(self, request):
        """
        Register a new user.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login', permission_classes=[])
    def login_user(self, request):
        """
        Log in an existing user.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'], url_path='logout', permission_classes=[])
    def logout_user(self, request):
        """
        Log out the current user.
        """
        logout(request)
        return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
        })

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        print("Request data:", request.data)
        try:
            return super().post(request, *args, **kwargs)
        except (InvalidToken, TokenError) as e:
            return Response({"error": str(e)}, status=400)


from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def validate_token(request):
    token = request.data.get('token', None)
    try:
        access_token = AccessToken(token)
        return Response({"message": "Token is valid"}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

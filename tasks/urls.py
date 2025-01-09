from django.urls import path, include
from .views import TaskListCreateView, TaskDetailView, TaskMarkCompleteView, TaskMarkIncompleteView
from .views import  UserListAPIView#, UserViewSet
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomAuthToken


from django.contrib.auth.views import LoginView, LogoutView


from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/auth/', obtain_auth_token),
    path('api/users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/mark-complete/', TaskMarkCompleteView.as_view(), name='task-mark-complete'),
    path('tasks/<int:pk>/mark-incomplete/', TaskMarkIncompleteView.as_view(), name='task-mark-incomplete'),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', UserListAPIView.as_view(), name='user-list'),  # Optional for superuser testing
    path('user/<int:pk>/', UserListAPIView.as_view(), name='specific-user'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('api/token-auth/', obtain_auth_token, name='token_auth'),
    path('api/token-auth/', CustomAuthToken.as_view(), name='token_auth'),
]

from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'users', UserViewSet,basename='user')# 


urlpatterns = [
    path('', include(router.urls)),
]

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns += [
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

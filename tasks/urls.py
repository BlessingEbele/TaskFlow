from django.urls import path, include
from .views import TaskListCreateView, TaskDetailView, TaskMarkCompleteView, TaskMarkIncompleteView
from .views import  UserListAPIView, UserViewSet
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomAuthToken

#from .views import TaskListCreateAPIView, TaskDetailAPIView,
from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# schema_view = get_schema_view(
#     openapi.Info(
#         title="TaskFlow API",
#         default_version='v1',
#         description="API documentation for TaskFlow",
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/mark-complete/', TaskMarkCompleteView.as_view(), name='task-mark-complete'),
    path('tasks/<int:pk>/mark-incomplete/', TaskMarkIncompleteView.as_view(), name='task-mark-incomplete'),
    path('api-auth/', include('rest_framework.urls')),
    # path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    # path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('users/', UserListAPIView.as_view(), name='user-list'),  # Optional for superuser testing
    path('user/<int:pk>/', UserListAPIView.as_view(), name='specific-user'),
    # path('register/', views.register_user, name='register-user'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('api/token-auth/', obtain_auth_token, name='token_auth'),
    # path('api/token-auth/', CustomAuthToken.as_view(), name='token_auth'),
]

from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]

"""
URL configuration for TaskFlowAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_viewis
from rest_framework.authtoken.views import obtain_auth_token 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', obtain_auth_token),  # Token Authentication Endpoint

]

#after frontend configuration
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns += [

    path('static/login.html/', LoginView.as_view(), name='login'),
    path('static/logout.html/', LogoutView.as_view(), name='logout'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/logout/', LogoutView.as_view(), name='logout'),
]

"""Django_REST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include,url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',schema_view),
    #path('/', views.api_root),
    
    path('api-auth/', include('rest_framework.urls')),

    path('users/', views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('envs/', views.EnvList.as_view(),name='env-list'),
    path('envs/<int:pk>/', views.EnvDetail.as_view()),

    path('pros/', views.ProjectList.as_view(),name='pro-list'),
    path('pros/<int:pk>/', views.ProjectDetail.as_view()),

    path('mods/', views.ModuleList.as_view(),name='mod-list'),
    path('mods/<int:pk>/', views.ModuleDetail.as_view()),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)

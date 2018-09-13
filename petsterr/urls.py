"""petsterr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('', include('web.urls', namespace='web')),
    path('base/', include('base.urls')),
    path('admin/', admin.site.urls),
    path('api/kennels/', include('kennels.api.urls', namespace='kennels')),
    path('api/animals/', include('animals.urls', namespace='animals')),
    path('api/litters/', include('litters.urls', namespace='litters')),
    path('api/v1/users/', include('users.api.urls', namespace='users')),
    path('api/countries/', include('countries.urls', namespace='countries')),
    path('api/clubs/', include('clubs.urls', namespace='clubs')),
    path('api/news/', include('news.urls', namespace='news')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token)

]

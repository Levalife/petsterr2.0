from django.urls import path, re_path

from . import views

app_name = "web"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^kennels/', views.IndexView.as_view()),
    re_path(r'^login/', views.IndexView.as_view(), name='login'),
    re_path(r'^signup/', views.IndexView.as_view(), name='signup'),
    re_path(r'^forgot_password/', views.IndexView.as_view(), name='forgot_password'),
    re_path(r'^dashboard/', views.IndexView.as_view(), name='dashboard'),
    re_path(r'^reset_password/', views.IndexView.as_view(), name='reset_password'),
]
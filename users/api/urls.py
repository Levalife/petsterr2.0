from django.urls import path

from users.api.views import UserCreateAPIView, UserLoginAPIView, UserChangePasswordAPIView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('change_password/', UserChangePasswordAPIView.as_view(), name='change_password'),
]
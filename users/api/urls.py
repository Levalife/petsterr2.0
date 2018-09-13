from django.urls import path

from users.api.views import UserCreateAPIView, UserLoginAPIView, UserLogoutAPIView, \
    UserResetPasswordAPIView, UserValidateTokenAPIView, UserForgotPasswordAPIView

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('forgot_password/', UserForgotPasswordAPIView.as_view(), name='forgot_password'),
    path('reset_password/', UserResetPasswordAPIView.as_view(), name='reset_password'),
    path('validate_token/', UserValidateTokenAPIView.as_view(), name='validate_token'),
]
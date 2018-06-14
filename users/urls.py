from django.urls import path

from users.ProfilesViews import ProfilesView
from users.views import LoginView, SignUpView, LogOutView
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogOutView.as_view(), name='logout_page'),
    path('profile/', ProfilesView.as_view(), name='profile_page'),
    path('signup/', SignUpView.as_view(), name='signup_page'),
]
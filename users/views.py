from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from users.UsersHandler import UsersHandler


class SignUpView(View):
    form_class = UserCreationForm
    handler = UsersHandler()

    def get(self, request, *args, **kwargs):
        context = dict(form=self.form_class, hide_authentiation=True)
        return render(request, 'users/signup.html', context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.handler.create_user(dict(username=form.cleaned_data.get('username'),
                                          email=form.cleaned_data.get('username'),
                                          password=form.cleaned_data.get('password1')))
            return HttpResponseRedirect(reverse('kennels:kennels_page'))
        context = dict(form=form, hide_authentiation=True)
        return render(request, 'users/signup.html', context=context)


class LoginView(View):
    form_class = AuthenticationForm
    handler = UsersHandler()

    def get(self, request, *args, **kwargs):
        context = dict(form=self.form_class, hide_authentiation=True)
        return render(request, 'users/login.html', context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            self.handler.login_user(request, form.cleaned_data)
            return HttpResponseRedirect(reverse('kennels:kennels_page'))
        context = dict(form=form, hide_authentiation=True)
        return render(request, 'users/login.html', context=context)


class LogOutView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return HttpResponseRedirect(reverse('web:index'))

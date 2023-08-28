from django.views.generic import CreateView
from .models import MyUser, ViewHistory
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

@login_required
def user_profile_view(request):
    user = request.user
    viewing_history = ViewHistory.objects.filter(user=user).order_by('-timestamp')
    return render(request, 'userapp/user_profile.html', {'user': user, 'viewing_history': viewing_history})


class CustomLoginView(LoginView):
    template_name = 'userapp/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class RegisterView(CreateView):
    model = MyUser
    form_class = RegisterForm
    template_name = 'userapp/register.html'
    success_url = '/login/'
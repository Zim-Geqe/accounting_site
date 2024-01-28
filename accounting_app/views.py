from django.shortcuts import render
from .models import Service
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import CustomUser
# from accounting_app.models import CustomUser


def landing(request):
    return render(request, 'landing.html')


def login_view(request):
    if request.method == 'POST':
    
        email = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "The email or password is incorrect.")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


@login_required 
def admin_dashboard(request):
    user_id = request.user.id
    admin_display = CustomUser.objects.get(id=user_id)
    users = CustomUser.objects.all()
    context = {'admin_display': admin_display,
               'users': users}
    
    return render(request, 'admin_dashboard.html', context)



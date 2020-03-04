from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import User, UserManager
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# renderとは render(request, path, context(省略可能))、目的:pathの画面をただ見せたい
def index(request):
    form = UserLoginForm()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'user_login.html', {'user': user})
                # Redirect to a success page.
            else:
                return render(request, 'user_login.html', {'user': user})
                # Return a 'disabled account' error message
        else:
            return render(request, 'user_login.html', {'user': user})
            # Return an 'invalid login' error message.
    
    return render(request, 'index.html', {'form': form})

def user_create(request):
    user = User()
    
    if request.method == "POST":
        form = UserCreateForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('account:index')
    else:
        form = UserCreateForm()
    return render(request, 'user_create.html', {'form': form})

def user_login(request):
    return render(request, 'user_login.html')

def user_logout(request):
    logout(request)
    # Redirect to a success page.
    form = UserLoginForm()
    return render(request, 'index.html', {'form': form})
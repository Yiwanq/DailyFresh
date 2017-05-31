from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'app_user/login.html')

def register(request):
    return render(request, 'app_user/register.html')

def user_center_info(request):
    return render(request, 'app_user/user_center_info.html')
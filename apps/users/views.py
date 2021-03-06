from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from users.models import UserProfile
from .forms import LoginForm,RegisterForm

# Create your views here.
class RegisterView(View):
    '''用户注册'''
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html', {'register_form': register_form})

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get("username", "")
#         pass_word = request.POST.get("password", "")
#         # 新增, 利用django自带的authenticate方法来确认这个用户是否合法, 如果合法, 则user是一个非空对象.
#         user = authenticate(username=user_name, password=pass_word)
#         if user is not None:
#             #django自带的login方法,
#             login(request,user)
#             #登录成功后返回首页
#             return render(request, "index.html")
#         else:
#             return render(request, "login.html",{"msg": "用户名或密码错误！"})
#     elif request.method == "GET":
#         # render 就是渲染html返回用户
#         return render(request, "login.html",{})

class LoginView(View):
    def get(self,request):
        return render(request,"login.html",{})
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            # 新增, 利用django自带的authenticate方法来确认这个用户是否合法, 如果合法, 则user是一个非空对象.
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)  # django自带的login方法,
                return render(request, "index.html")  # 登录成功后返回首页
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})
        else:
            return render(request,"login.html", {"login_form": login_form})


import random

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from myproject_test.models import MyprojectTestStudentinfo


def home(request):
    return HttpResponse('Hello, World!')

def toLogin_view(request):
    return render(request, 'login.html')

def Login_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')
    print(u)
    if u and p:
        c = MyprojectTestStudentinfo.objects.filter(stu_name=u, stu_psw=p).count()
        if c >= 1:
            return HttpResponse("登陆成功!")
        else:
            return HttpResponse("账号密码错误！")
    else:
        return HttpResponse("请输入正确的账号和密码")

#渲染注册界面
def toRegister_view(request):
    return render(request, 'register.html')

# 点击注册后做的逻辑判断
def Register_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')
    print(u)
    if u and p:
        stu = MyprojectTestStudentinfo(stu_name=u, stu_psw=p)
        stu.save()
        return HttpResponse("注册成功")
    else:
        return HttpResponse("请输入完整的账号与密码:")


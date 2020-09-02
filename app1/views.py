from django.http import HttpResponse


# Create your views here.


def index(request):
    print("11111")

    return HttpResponse("test")


def user_login(request):

    print("用户登录成功")

    return HttpResponse("跳转到项目首页")


def test_dev(request):

    pri

    return HttpResp
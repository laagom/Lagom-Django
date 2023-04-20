from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

from shortener.models import Users
from shortener.register.form import RegisterForm

# Create your views here.

def index_view(request):
    ''' 
    URL 요청을 통한, Index 화면이동 예시
    '''
    user = Users.objects.filter(username=request.user).first()
    email = user.email if user else "Anonymous User!"

    print("Logged in?", request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = "Anonymous User!"

    return render(request, "index.html", {"user" : f" {email}!"})


def redirect_view(request):
    '''
    화면 이동 시, render와 redirect의 차이 예시
    '''
    print("진입 redirect_view")
    
    return redirect("index")


@csrf_exempt  # csrf예외 처리 : JWT 토큰 발생 시 csrf 토큰이 필요 없다. 
def get_user(request, user_id):
    '''
    HTTP method GET, POST를 사용하여 사용자 정보 조회
    '''
    if request.method == 'GET':
        abc = request.GET.get("abc")
        xyz = request.GET.get("xyz")
        user = Users.objects.filter(pk=user_id).first()
        return render(request, "base.html", {"user" : user,  "params" : [abc, xyz]})
    elif request.method == 'POST':
        username = request.GET.get("username")
        if username:
            user = Users.objects.filter(pk=user_id).update(username=username)

        return JsonResponse(status=201,data=dict(msg="You just reached with Post Method!"), safe=False)
    

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        msg = "올바르지 않은 데이터 입니다."

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg = "회원가입완료"
        return render(request, "register.html", {"form" : form, "mag" : msg})
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form" : form})
        
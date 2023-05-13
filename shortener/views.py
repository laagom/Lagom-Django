from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from shortener.models import PayPlan, Users
from shortener.forms.form import LoginForm, RegisterForm

# Create your views here.

@login_required
def index_view(request):
    ''' 
    URL 요청을 통한, Index 화면이동 예시
    '''
    user = Users.objects.filter(username=request.user).first()
    email = user.email if user else "Anonymous User"

    print("Logged in?", request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = "Anonymous User"

    return render(request, "index.html", {"user" : user})


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
    

def register_view(request):
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
        

def login_view(request):
    is_ok = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        template = "login.html"
        if form.is_valid():
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password")
            remember_me = form.cleaned_data.get("remember_me")
            msg = "올바른 유저ID와 패스워드를 입력하세요."
            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
                pass
            else:
                if user.check_password(raw_password):
                    msg = None
                    login(request, user)
                    is_ok = True
                    request.session["remember_me"] = remember_me
                    
                    # 브라우저가 닫혔을 때, 세션 만료 시간 설정(edge에서 테스트 진행)
                    if not remember_me:
                        request.session.set_expirey(1)
    else:
        msg = None
        form = LoginForm()
    print("REMEMBER_ME: ", request.session.get("remember_me"))
    return render(request, "login.html", {"form": form, "msg": msg, "is_ok": is_ok})


def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def payplan_list_view(request):
    page = int(request.GET.get("page", 1))
    pay_plans = PayPlan.objects.all().order_by("-id")
    paginator = Paginator(pay_plans, 10, orphans=9)
    pay_plans = paginator.get_page(page)

    return render(request, "payplan/boards.html", {"pay_plans": pay_plans})

@login_required
def user_list_view(request):
    page = int(request.GET.get("page", 1))
    users = Users.objects.all().order_by("-id")
    paginator = Paginator(users, 10)
    users = paginator.get_page(page)

    return render(request, "user/boards.html", {"users": users})
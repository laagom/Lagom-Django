from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from shortener.models import PayPlan, Users
from shortener.register.form import RegisterForm

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
    msg = None
    is_ok = False
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        template = "login.html"
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                template = "index.html"
                is_ok = True
        else:
            msg = "올바른 유저ID와 패스워드를 입력하세요."

    else:
        form = AuthenticationForm()
    
    for visible in form.visible_fields():
        visible.field.widget.attrs["placeholder"] = "유저ID" if visible.name == "username" else "패스워드"
        visible.field.widget.attrs["class"] = "form-control"
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
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from shortener.models import Users

# Create your views here.

def index_view(request):
    ''' 
    URL 요청을 통한, 화면이동 예시
    '''
    print("진입 index_view")
    print(request.user.pay_plan.name)

    user = Users.objects.filter(username='admin').first()
    email = user.email if user else "Anonymous User!"
    print("Logged in?", request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = "Anonymous User!"
    print(email)
    return render(request, "index.html", {"welcome_msg" : f"Hello {email}!", "hello" : "World"})


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
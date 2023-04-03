from django.shortcuts import render, redirect

from shortener.models import Users

# Create your views here.
# 함수작성 시 request는 필수로 인수로 전달 받아야 한다.
# views까지 들어올 때 여러 middle을 거치는데 middle에서 request를 넘기기 때문이다.
def index_view(request):
    print("진입 index_view")

    # filter, get 두개다 orm으로 데이터를 조회 하는 방법이지만 get의 경우 없는 값이 들어오는 경우
    # 에러가 발생하기 때문에 반드시 한 개만 존재하는 경우에 사용한다.
    # valudation용으로 많이 사용한다.
    # user = Users.objects.filter(username='admin').first()
    user = Users.objects.get(username='admin1')
    email = user.email if user else "Anonymous User!"

    print(email)
    # request 안에 들어있는 user의 is_authenticated는 로그인이 되어 있는지 확인한다.
    print(request.user.is_authenticated)
    # if request.user.is_authenticated is False:
    #     email = "Anonymous User!"
    #     print(email)
    
    # render넘겨주는 인자 request(요청), template(템플릿), context(메시지)
    return render(request, "index.html", {"welcome_msg" : f"Hello {email}!", "hello" : "World"})


def redirect_view(request):
    print("진입 redirect_view")
    
    # view단에 있는 index가 아닌 urls.py 에서 명명한 name=index 이다.
    # redirect의 용도 : 권한이 없거나 로그인이 되어 있지 않은데 로그인이 필요한 
    #                  화면에 접근하려 할때 redirect로 이동 시킬 수 있다.
    return redirect("index")
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

"""
1. def login 뷰를 생성
2. member app을 include를 이용해 'member' namespace를 지정
    instagram/urls.py와 member/ulrs.py 모두 사용
3. login 뷰는 member/login URL과 연결되도록 member/urls.py 구현
4. login 뷰에서는 member/login.html 파일을 렌더함
5. settings.py에 TEMPLATE_DIR 변수를 할당하고 추가

과제 : 폼을 이용해 정상적으로 동작하게 해오기
html파일에서 POST 요청을 보내기 위해서 form을 정의하고
input 요소 2개의 name을 username, password로 설정하고
button type submit을 실행
(login.html에 작성하면됨)
"""


def login_fbv(request):
    """
    request.method == 'POST'일 때와 아닐 때의 동작을 구분
    POST일 때는 authenticate, login을 거치는 로직을 실행
    GET일 때는 member/login.html을 render하여 return 한다.
    """

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # authenticate 인자로 POST로 전달받은 username, password 사용
            user = authenticate(username=username, password=password)
            if user is not None:
                # 장고의 인증관리 시스템을 이용하여 세션을 관리해주기 위해 login() 함수 사용
                login(request, user)
                # return HttpResponse('Login Success')
                return redirect('/admin')
            else:
                form.add_error(None, 'ID or PW incorrect')
                # return HttpResponse('Login Failed')
    # GET method 요청이 온 경우
    else:
        # 빈 login form 객체를 생성
        form = LoginForm()
    context = {
        'form': form,
    }
    # return render(request, 'member/login.html')
    return render(request, 'member/login.html', context)

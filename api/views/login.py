from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import auth
from rest_framework.authtoken.models import Token
from api.models import UserInfo


class LoginView(APIView):
    def post(self, request):
        res = {
            'code': 412,
            'msg': '登录成功！',
            'data': [],
            'userid': '',
            'username': '',
            'role': '',
            'token': '',
        }

        user = auth.authenticate(**request.data)
        if not user:
            res['msg'] = '用户名或密码错误'
            return Response(res)

        old_token = Token.objects.filter(user=user)
        old_token.delete()
        token = Token.objects.create(user=user)
        auth.login(request, user)
        res['code'] = 200
        res['userid'] = user.nid
        res['username'] = user.username
        res['token'] = token.key,
        res['role'] = user.role,

        return Response(res)


class SignView(APIView):
    def post(self, request):
        res = {
            'code': 412,
            'msg': '注册成功！',
            'data': [],
            'userid': '',
            'username': '',
            'role': '',
            'token': '',
        }
        username = request.data.get('username')
        password = request.data.get('password')
        rePassword = request.data.get('rePassword')

        user_obj = UserInfo.objects.filter(username=username).first()
        if user_obj:
            res['msg'] = '该用户名已存在'
            return Response(res)

        if password != rePassword:
            res['msg'] = '两次密码输入不一致'
            return Response(res)
        user = UserInfo.objects.create_user(username=username, password=password)
        token = Token.objects.create(user=user)
        res['userid'] = user.nid
        res['username'] = username
        res['role'] = user.role
        res['token'] = token.key
        res['code'] = 200
        return Response(res)


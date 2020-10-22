
"""
中间件的作用: 每次请求和相应的时候都会调用

中间件的定义

中间件的使用: 我们可以判断每次请求中是否携带了cookie中某些信息

"""
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


def simple_middleware(get_response):

    # 这里是 中间件第一次调用执行的地方
    # print('init1111')

    def middleware(request):
        # username = request.COOKIES.get('username')
        # if username is None:
        #     print('username is None')
        #     return HttpResponse('哥们,你没有登陆哎')
        # 这里是 请求前
        print('before request 1111111111111111')
        response=get_response(request)
        #这里就 响应后/请求后
        print('after request/response 111111111111')
        return response


    return middleware

def simple_middleware2(get_response):
    # print('init2222')

    def middleware(request):
        # username = request.COOKIES.get('username')
        # if username is None:
        #     print('username is None')
        #     return HttpResponse('哥们,你没有登陆哎')
        # 这里是 请求前
        print('before request 22222222222222')
        response=get_response(request)
        #这里就 响应后/请求后
        print('after request/response 222222222222222')
        return response


    return middleware

class SimpleMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('before request ........')

    def process_response(self, request, response):
        print('after request ........')

        return response

import json
from datetime import datetime

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

def demo(request):

    return HttpResponse('demo')

def index(request):

    """
    reverse  就是通过 name 来动态获取路径(路由)
    如果没有设置namespace 则可以通过name来获取 reverse(name)
    如果有设置namespace 则可以通过namespace:name来获取 reverse(namespace:name)

    # 登陆成功之后需要跳转到首页
    # 注册成功之后需要跳转到首页
    """
    # viewname 通过视图名字
    # 路由是动态获取的
    # path = reverse('index')
    # print(path)

    #如果我们设置了namespance 这个时候就需要通过 namespace:name 来获取路由
    # path=reverse('book:index')
    # print(path)
    # 跳转页面
    # 登陆成功之后需要跳转到首页
    # return redirect('/home/')
    # return redirect(path)


    # 注册成功之后需要跳转到首页
    # return redirect('/home/')
    # return redirect(path)


    return HttpResponse("index")



def detail(request,book_id,category_id):

    # 1/100/
    # print(category_id,book_id)


    ###########################GET 查询字符串#################################
    """
    https://www.baidu.com/s?ie=utf-8&wd=itcast&rsv_pq=fdf543ed000f8688&rsv_t=8862Eb1lxc9858Ihke7VdJylicTyYs%2F3EuFyVPKcOBnv9wmTxLdhwlYL6%2F8&rqlang=cn&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100

    以? 作为一个分隔
    ?前边 表示 路由
    ?后边 表示 get方式传递的参数 称之为 查询字符串
    ?key=value&key=value...

    我们在登陆的时候会输入用户名和密码 理论上 用户名和密码都应该以POST方式进行传递
    只是为了让大家好理解,我们接下来 用 get方式来传递用户名和密码
    """

    # query_params = request.GET
    # print(query_params)
    # #QueryDict: {'username': ['itcast'], 'password': ['123']}
    #
    # #QueryDict
    # #<QueryDict: {'username': ['itcast', 'itheima'], 'password': ['123']}>
    #
    # # QueryDict 以普通的字典形式来获取 一键多值的是时候 只能获取最后的那一个值
    # # 我们想获取 一键一值的化 就需要使用 QueryDict 的get方法
    # # 我们想获取 一键多值的化 就需要使用 QueryDict 的getlist方法
    # username=query_params['username']
    # password=query_params.get('password')
    #
    # # print(username,password)
    #
    # # print(username)
    #
    # users = query_params.getlist('username')
    # print(users)

    ###########################POST 表单数据#################################

    # data = request.POST
    # print(data)

    ###########################POST json数据#################################
    """
    JSON 是双引号
    {
        "name":"itcast"
    }
    """

    # print(request.POST)
    # body=request.body
    # b'{\n    "username":"itcast",\n    "passwrod":"123"\n}'
    # body_str = body.decode()  # JSON形式的字符串
    """
    {
        "username":"itcast",
        "passwrod":"123"
    }
    """
    # print(type(body_str))
    # print('~~~~~~~')
    # print(body_str['username'])

    """
    json
    json.dumps   将字典转换为 JSON形式的字符串
    json.loads   将JSON形式的字符串 转换为字典
    """
    # data = json.loads(body_str)
    # print(data)
    ###########################请求头#################################

    # print(request.META)
    #
    # content_type=request.META['CONTENT_TYPE']
    # print(content_type)

    # print(request.method)
    #
    # print('我是有底线的~~~')

    ###########################跳转页面#################################

    # 需求是跳转到首页
    # 通过reverse 这个名字来找到路径
    path = reverse('book:index')
    return redirect(path)

    return redirect('/index/')

    # return redirect('http://www.itcast.cn')

    ###########################JsonResponse#################################
    from django.http import JsonResponse
    data = {'name': 'itcast'}

    return JsonResponse(data)

    ###########################HttpResponse#################################
    data = {'name':'itcast'}
    # HttpResponse
    # content       传递字符串 不要传递 对象,字典等数据
    # statue        HTTP status code must be an integer from 100 to 599. 只能使用系统规定的
    # content_type  是一个MIME类型
    #               语法形式是: 大类/小类
    #   text/html   text/css    text/javascript
    #   application/json
    #   image/png   image/gif   image/jpeg
    return HttpResponse(data,status=400)


"""
面试题:
    你是如何理解cookie的? / 你谈一谈cookie/

    1. 概念
    2. 流程 (大体流程,从http角度分析)
    3. 在开发过程中哪里使用了
    4. 你在开发过程中遇到什么印象深刻的地方

保存在客户端的数据叫做 cookie

    cookie是保存在客户端
    cookie是基于域名(IP)的


    0.概念
    1.流程(原理)

        第一次请求过程
        ① 我们的浏览器第一次请求服务器的时候,不会携带任何cookie信息
        ② 服务器接收到请求之后,发现 请求中没有任何cookie信息
        ③ 服务器设置一个cookie.这个cookie设置响应中
        ④ 我们的浏览器接收到这个相应之后,发现相应中有cookie信息,浏览器会将cookie信息保存起来

        第二次及其之后的过程
        ⑤ 当我们的浏览器第二次及其之后的请求都会携带cookie信息
        ⑥ 我们的服务器接收到请求之后,会发现请求中携带的cookie信息,这样的话就认识是谁的请求了

    2.看效果

    3.从http协议角度深入掌握cookie的流程(原理)

        第一次
            ① 我们是第一次请求服务器,不会携带任何cookie信息,请求头中没有任何cookie信息
            ② 服务器会为响应设置cookie信息.   响应头中有set_cookie信息

        第二次及其之后的
            ③ 我们第二次及其之后的请求都会携带cookie信息,请求头中有cookie信息
            ④(可选) 在当前我们的代码中,没有再 在相应头中设置cookie,所以响应头中没有set_cookie信息
"""

def set_cookie(request):
    """
    # 第一次请求过程
    # ① 我们的浏览器第一次请求服务器的时候,不会携带任何cookie信息
    # ② 服务器接收到请求之后,发现 请求中没有任何cookie信息
    # ③ 服务器设置一个cookie.这个cookie设置在响应中
    # ④ 我们的浏览器接收到这个相应之后,发现相应中有cookie信息,浏览器会将cookie信息保存起来
    """
    #1. 先判断有没有cookie信息
    # 先假设就是没有
    #request.COOKIES

    #2.获取用户名
    username=request.GET.get('username')
    #3. 因为我们假设没有cookie信息,我们服务器就要设置cookie信息
    response = HttpResponse('set_cookie')

    # key,value
    # max_age 单位是秒
    # 时间是 从服务器接收到这个请求时间 + 秒数 计算之后的时间
    response.set_cookie('username',username,max_age=3600)


    #删除cookie的2种方式
    # response.delete_cookie(key)
    # response.set_cookie(key,value,max_age=0)

    #4.返回相应
    return response



def get_cookie(request):
    """

    # 第二次及其之后的过程
    # ⑤ 当我们的浏览器第二次及其之后的请求都会携带cookie信息
    # ⑥ 我们的服务器接收到请求之后,会发现请求中携带的cookie信息,这样的话就认识是谁的请求了

    """

    #1.服务器可以接收(查看)cookie信息
    cookies = request.COOKIES
    # cookies 就是一个字典
    username=cookies.get('username')

    #2. 得到用户信息就可以继续其他的业务逻辑了

    return HttpResponse('get_cookie')



"""
    问题1: 我换了浏览器,还能获取到 session信息吗? 不可以

    问题2: 我不换浏览器,删除session id ,则获取不到session数据

    问题3: 再去执行 set_sesison 的时候 会重新生成session id


保存在服务器的数据叫做 session
    session需要依赖于cookie

    如果浏览器禁用了cookie,则session不能实现

    0.概念
    1.流程

        第一次请求:
            ① 我们第一次请求的时候可以携带一些信息(用户名/密码) cookie中没有任何信息
            ② 当我们的服务器接收到这个请求之后,进行用户名和密码的验证,验证没有问题可以设置session
                信息
            ③ 在设置session信息的同时(session信息保存在服务器端).服务器会在响应头中设置一个 sessionid 的cookie信息(由服务器自己设置的,不是我们设置的)
            ④ 客户端(浏览器)在接收到响应之后,会将cookie信息保存起来(保存 sessionid的信息)




        第二次及其之后的请求:
            ⑤ 第二次及其之后的请求都会携带 session id信息
            ⑥ 当服务器接收到这个请求之后,会获取到sessionid信息,然后进行验证,
                验证成功,则可以获取 session信息(session信息保存在服务器端)

    2.效果



    3.从原理(http)角度

        第一次请求:
            ① 第一次请求,在请求头中没有携带任何cookie信息
            ② 我们在设置session的时候,session会做2件事.
                #第一件：　将数据保存在数据库中
                #第二件：　设置一个cookie信息，这个cookie信息是以　sessionid为key  value为 xxxxx
                cookie肯定会以响应的形式在相应头中出现

        第二次及其之后的:

            ③ 都会携带 cookie信息,特别是 sessionid


"""
def set_session(request):

    """
     第一次请求:
            ① 我们第一次请求的时候可以携带一些信息(用户名/密码) cookie中没有任何信息
            ② 当我们的服务器接收到这个请求之后,进行用户名和密码的验证,验证没有问题可以设置session
                信息
            ③ 在设置session信息的同时(session信息保存在服务器端).服务器会在响应头中设置一个 sessionid 的cookie信息
            ④ 客户端(浏览器)在接收到响应之后,会将cookie信息保存起来(保存 sessionid的信息)

    """
    # 1.cookie中没有任何信息
    print(request.COOKIES)

    #2.对用户名和密码进行验证
    # 假设认为 用户名和密码正确
    user_id=6666

    #3.设置session信息
    # request.session  理解为字典
    # 设置session的时候其实 session做了2件事
    #第一件：　将数据保存在数据库中
    #第二件：　设置一个　ｃｏｏｋｉｅ信息，这个ｃｏｏｋｉｅ信息是以　sessionid为key
    request.session['user_id']=user_id

    #4. 返回响应
    return HttpResponse('set_session')



def get_session(request):

    """


        第二次及其之后的请求:
            ⑤ 第二次及其之后的请求都会携带 session id信息
            ⑥ 当服务器接收到这个请求之后,会获取到sessionid信息,然后进行验证,
                验证成功,则可以获取 session信息(session信息保存在服务器端)

    """
    #1. 请求都会携带 session id信息
    print(request.COOKIES)

    #2. 会获取到sessionid信息,然后进行验证,
    # 验证成功,可以获取 session信息(

    # request.session 字典
    user_id=request.session['user_id']
    user_id=request.session.get('user_id')

    #

    #3.返回响应
    return HttpResponse('get_session')



"""
登陆页面
    GET 请求是获取 登陆的页面
    POST 请求是 验证登陆 (用户名和密码是否正确)
"""

# GET 请求是获取 登陆的页面
def show_login(request):

    return render(request)

#POST 请求是 验证登陆 (用户名和密码是否正确)
def veri_login(request):

    return redirect('首页')


# 我想由2个视图 变为 1个视图

def login(request):

    #我们需要区分业务逻辑
    if request.method == 'GET':
        # GET 请求是获取 登陆的页面
        return render(request)

    else:
        # POST 请求是 验证登陆 (用户名和密码是否正确)
        return redirect('首页')


"""
面向对象

    类视图 是采用的面向对象的思路

    1.定义类试图
        ① 继承自 View  (from django.views import View)
        ② 不同的请求方式 有不同的业务逻辑
            类试图的方法 就直接采用 http的请求方式的名字 作为我们的函数名.例如: get ,post,put,delete
        ③  类试图的方法的第二个参数 必须是请求实例对象
            类试图的方法 必须有返回值 返回值是HttpResopnse及其子类

    2.类试图的url引导
"""
from django.views import View
class BookView(View):

    def get(self,request):

        username=request.COOKIES.get('username')
        if username is None:
            print('username is None')
        return HttpResponse('get')


    def post(self,request):
        username = request.COOKIES.get('username')
        if username is None:
            print('username is None')
        return HttpResponse('post')


    def put(self,request):
        username = request.COOKIES.get('username')
        if username is None:
            print('username is None')
        return HttpResponse('put')

    def oooo(self,request):

        return HttpResponse('oooo')



class Person(object):

    # cls 是谁? --> Person 类
    @classmethod
    def say(cls):
        pass


    # self 是谁? --> 实例对象
    def eat(self):
        pass


    @staticmethod
    def run():
        pass

Person.say()

p=Person()
p.eat()


"""
个人中心页面      --  必须登陆才能显示
GET 方式 展示 个人中心
POST 实现个人中心信息的修改
定义类视图
"""
from django.contrib.auth.mixins import LoginRequiredMixin

class CenterView(LoginRequiredMixin,View):

    def get(self,request):

        return HttpResponse('个人中心展示')

    def post(self,request):

        return HttpResponse('个人中心修改')

#############################模板############################################

class HomeView(View):

    def get(self,request):

        #1.获取数据
        username=request.GET.get('username')

        #2.组织数据
        context = {
            'username':username,
            'age':14,
            'birthday':datetime.now(),
            'firends':['tom','jack','rose'],
            'money':{
                '2019':12000,
                '2020':18000,
                '2021':25000,
            },
            'desc':'<script>alert("hot")</script>'
        }

        # return render(request,'detail.html')
        return render(request,'index.html',context=context)

















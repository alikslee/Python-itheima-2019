from django.urls import path, re_path

from book import views
from book.views import index, set_cookie, get_cookie, set_session, get_session, BookView, CenterView, HomeView, detail

app_name = 'book'

urlpatterns = [
    # name 就是给url起一个名字
    # 我们可以通过name找到这个路由
    re_path(r'^home/$', index, name='index'),

    # http://127.0.0.1:8000/分类id/书籍id/
    # http://127.0.0.1:8000/category_id/book_id/
    # 分组来获取正则中的数据
    # 根据位置来获取 url中的参数
    # url(r'^(\d+)/(\d+)/$',detail),

    # 关键字参数--推荐大家使用关键字参数
    re_path(r'^(?P<category_id>\d+)/(?P<book_id>\d+)/$', detail),

    # cookie的第一次请求
    re_path(r'^set_cookie/$', set_cookie),

    # cookie的第二次及其之后的请求
    re_path(r'^get_cookie/$', get_cookie),

    re_path(r'^set_session/$', set_session),
    re_path(r'^get_session/$', get_session),

    # url的第一个参数是 正则
    # url的第二个参数是 视图函数名
    re_path(r'^login/$', BookView.as_view()),

    re_path(r'^center/$', CenterView.as_view()),

    re_path(r'^index/$', HomeView.as_view()),
]


#coding: utf-8

from django.shortcuts import render, redirect, HttpResponseRedirect
from df_user.models import *
from hashlib import sha1
from django.http import JsonResponse
from django.core.paginator import Paginator



#register请求页面
def register(request):
    return render(request, 'df_user/register.html')

#将用户注册的内容进行保存
def register_handle(request):
    """接收用户输入信息"""
    post = request.POST
    uname = post.get('user_name')  #用户名
    upwd = post.get('pwd')     #密码
    ucpwd = post.get('cpwd')    #确认密码
    uemail = post.get('email')    #email
    #判断两次用户输入的密码是否一致
    if upwd != ucpwd:
        return redirect('/user/register')   #如果两次密码不一致，直接重定向到注册页面
    #密码加密
    # s1 = sha1()
    # s1.update(upwd)
    # upwd2 = s1.hexdigest()
    # 如果密码一致，创建对象
    user = UserInfo()
    user.uname = uname
    # user.upwd = upwd2
    user.upwd = ucpwd
    user.upwd = upwd
    user.uemail = uemail
    user.save()
    #注册成功，跳转到登陆页面
    return redirect('/user/login')

#判断用户是否存在
def register_exist(request):
    uname = request.GET.get('uname')   #用get请求接收传回的数据
    count = UserInfo.objects.filter(uname=uname).count()   #用户传回的信息去匹配用户信息
    return JsonResponse({'count':count})   #直接返回一个字典

#跳转到登陆页面
def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登陆', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, 'df_user/login.html', context)


#登陆处理
# def login_handle(request):
#     """接收请求信息"""
#     get = request.POST
#     uname = get.get('username')
#     upwd = get.get('pwd')
#     jizhu = get.get('jizhu', 0)
#     #根据用户名查询对象
#     #如果使用filter如果没有查到返回None，如果使用get没有查到的话会抛出异常，所以需要使用try来捕捉异常
#     users = UserInfo.objects.filter(uname=uname)
#     print(uname)
#     #判断，如果未能查到，则用户名错误，查到再判断密码是否正确，正确则转到用户中心
#     if len(users) ==1:
#         s1 = sha1()
#         s1.update(upwd)
#         if s1.hexdigest() == users[0].upwd:
#             red = HttpResponseRedirect('/user/info')
#             #记住用户名
#             if jizhu != 0:
#                 red.set_cookie('uname', uname)
#             else:
#                 red.set_cookie('uname', '', max_age=-1)
#             request.session['user_id'] = users[0].id
#             request.session['user_name'] = uname
#             return red
#         else:
#             context = {'title': '用户登陆', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
#             return render(request, 'df_user/login.html', context)
#     else:
#         context = {'title': '用户登陆', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
#         return render(request, 'df_user/login.html', context)


def login_handle(request):
    get = request.POST
    uname = get.get('username')
    upwd = get.get('pwd')
    jizhu = get.get('jizhu', 0)
    users = UserInfo.objects.filter(uname = uname)
    print(uname)
    if len(users) == 1:
        red = HttpResponseRedirect('/user/info')
        if jizhu != 0:
            red.set_cookie('uname', uname)
        else:
            red.set_cookie('uname', '', max_age=-1)
        request.session['user_id'] = users[0].id
        request.session['user_name'] = uname
        return red
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
        return render(request, 'df_user/login.html', context)


#登陆用户中心
def info(request):
    user_email = UserInfo.objects.get(id = request.session['user_id']).uemail
    context = {'title': '用户中心',
               'user_email': user_email,
               'user_name': request.session['user_name']}
    return render(request, 'df_user/user_center_info.html', context)

#订单
def order(request):
    context = {'title': '用户中心'}
    return render(request, 'df_user/user_center_order.html', context)

#收获地址
def site(request):
    user = UserInfo.objects.get(id = request.session['user_id'])   # 根据id查找user对象
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubain = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title': '用户中心', 'user': user}
    return render(request, 'df_user/user_center_site.html', context)

# def logout(request):
#     request.session.flush()
#     return redirect('/')
#
# def user_center_order(request, pagedi):
#     """
#     此页面用户展示用户提交订单，由购物车页面下单后转调过来，也可以从个人信息页面查看
#     根据用户订单是否支支付，下单顺序进行排序
#     """
#     uid = request.session.get('user_id')
#     #订单信息，根据是否支付，下单顺序进行排序











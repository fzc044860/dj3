from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,HttpResponse,redirect

class AuthMiddleware(MiddlewareMixin):
    '''登陆验证中间件'''
    def process_request(self,request):
        #0、排除那些当不需要登陆的页面
        #request.path_info当前用户访问的url
        if request.path_info in ['/login/','/img/code/']:
            return
        #1、读取当前访问用户的session信息，如果能读得到说明已经登陆过
        info_dict = request.session.get("info")
        if info_dict:
            return
        #2、没有读到就返回登陆页
        return redirect('/login/')



"""dj3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from app01 import views
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 部门管理
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    # http://127.0.0.1:8000/2/edit/
    path('depart/<int:nid>/edit/', views.depart_edit),
    path('test/', views.test),

    # 用户管理
    path('user/list/', views.user_list),
    path('user/add/', views.user_add),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/<int:nid>/delete/', views.user_delete),

    # 靓号管理
    path('perttynum/list/', views.perttynum_list),
    path('perttynum/add/', views.perttynum_add),
    path('perttynum/<int:nid>/edit/', views.perttynum_edit),
    path('perttynum/<int:nid>/delete/', views.perttynum_delete),

    # 管理员管理
    path('admin/list/', views.admin_list),
    path('admin/add/', views.admin_add),
    path('admin/<int:nid>/edit/', views.admin_edit),
    path('admin/<int:nid>/delete/', views.admin_delete),
    path('admin/<int:nid>/reset/', views.admin_reset),

    # 登陆
    path('login/', views.login),
    path('logout/', views.logout),

    # 验证码
    path('img/code/', views.img_code),

    # 任务管理
    path('task/list/', views.task_list),
    path('task/ajax/', views.task_ajax),
    path('task/add/', views.task_add),

    # 订单管理
    path('order/list/', views.order_list),
    path('order/add/', views.order_add),
    path('order/delete/', views.order_delete),
    path('order/detail/', views.order_detail),

    # 数据统计
    path('chart/list/', views.chart_list),
    path('chart/bar/', views.chart_bar),
    path('chart/pie/', views.chart_pie),
    path('chart/line/', views.chart_line),

    #文件上传
    path('upload/list/',views.upload_list),
    path('depart/muti/',views.depart_muti),
    path('upload/form/',views.upload_form),
    path('upload/modelform/',views.upload_modelform),
    path('city/list/',views.city_list),
    path('city/add/',views.city_add),


    #设置media目录
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]

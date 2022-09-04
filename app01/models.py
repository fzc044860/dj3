from django.db import models

# Create your models here.
class Admin(models.Model):
    '''管理员'''
    username = models.CharField(verbose_name='帐号',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)
    def __str__(self):
        return self.username

class DepartMent(models.Model):
    '''部门表'''
    title = models.CharField(verbose_name='标题',max_length=32)
    def __str__(self):
        return self.title
class UserInfo(models.Model):
    '''员工表'''
    name = models.CharField(verbose_name='姓名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='帐户余额',max_digits=10,decimal_places=2,default=0) #总数10，小数位2
    #creat_time = models.DateTimeField(verbose_name='入职时间')  #年月日时分秒
    creat_time = models.DateField(verbose_name='入职时间') #年月日

    #没约束
    #depart_id = models.BigIntegerField(verbose_name='部门ID')

    #有约束
    #查空
    #depart = models.ForeignKey(to='DepartMent',to_field='id',null=True,blank=True,on_delete=models.SET_NULL())
    #级联删除
    depart = models.ForeignKey(verbose_name='部门', to='DepartMent',to_field='id',on_delete=models.CASCADE)

    gender_choices = (
        (1,'男'),
        (2,'女')
    )
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices,default=1)

class PrettyNum(models.Model):
    '''靓号表'''
    #想要字段允许为空就加上 null=True,blank=True
    mobile = models.CharField(verbose_name='手机号',max_length=32)
    price = models.IntegerField(verbose_name='价格',default=0)
    level_choices=(
        (1,'一级'),
        (2, '二级'),
        (3, '三级'),
        (4, '四级'),
        (5, '五级')
    )
    level = models.SmallIntegerField(verbose_name='级别',choices=level_choices,default=1)
    status_choices = (
        (1,'未占用'),
        (2, '已占用')
    )
    status = models.SmallIntegerField(verbose_name='状态',choices=status_choices,default=1)

class Task(models.Model):
    '''任务管理'''
    level_choices=(
        (1,'紧急'),
        (2, '一般'),
        (3, '临时'),
    )
    title = models.CharField(verbose_name='标题',max_length=64)
    detail = models.TextField(verbose_name='任务详情')
    level = models.SmallIntegerField(verbose_name='级别',choices=level_choices,default=3)
    user = models.ForeignKey(verbose_name='负责人',to="Admin",to_field="id",on_delete=models.CASCADE,default=1)

class Order(models.Model):
    '''工单'''
    oid = models.CharField(verbose_name='订单号',max_length=64)
    title = models.CharField(verbose_name='名称',max_length=32)
    price = models.IntegerField(verbose_name='价格')
    status_choices = (
        (1,"待支付"),
        (2, "已支付")
    )
    status = models.SmallIntegerField(verbose_name='状态',choices=status_choices,default=1)
    admin = models.ForeignKey(verbose_name='管理员',to='Admin',on_delete=models.CASCADE,default=1) #级联删除，当管理员表删除订单也会删除

class Boss(models.Model):
    '''老板'''
    name = models.CharField(verbose_name='姓名',max_length=32)
    age = models.IntegerField(verbose_name='年龄')
    img = models.CharField(verbose_name='头像',max_length=128)

class City(models.Model):
    '''城市，基于modelForm的上传示例'''
    name = models.CharField(verbose_name='名称',max_length=32)
    count = models.IntegerField(verbose_name='人口')
    #FileField 数据库本质也是CharField,自动保存数据
    img = models.FileField(verbose_name='LOGO',max_length=128,upload_to='city/')


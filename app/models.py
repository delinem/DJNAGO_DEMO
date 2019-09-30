from django.db import models
from django.contrib.auth.models import User

# Create your models here.

METHOD =['GET','POST','PUT','DELETE']



class Env(models.Model):
    env_id = models.AutoField(primary_key=True,verbose_name='序号')
    env_name = models.CharField(max_length=20,verbose_name='名称')
    env_address = models.CharField(max_length=100,verbose_name='地址')
    env_status = models.BooleanField(default=True,verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    owner = models.ForeignKey('auth.User', related_name='envs', on_delete=models.CASCADE,verbose_name='创建人')
    update_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    remake = models.CharField(max_length=100,verbose_name='备注')

    def __str__(self):
        return self.env_name
    
    class Meta:
        verbose_name ='环境信息'
        verbose_name_plural= verbose_name


class Project(models.Model):
    pro_id = models.AutoField(primary_key=True,verbose_name='序号')
    pro_name= models.CharField(max_length=50,verbose_name='名称')
    pro_code = models.CharField(max_length=50,verbose_name='编码') 
    pro_status = models.BooleanField(default=True,verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    owner = models.ForeignKey('auth.User', related_name='pro', on_delete=models.CASCADE,verbose_name='创建人')
    update_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    remake = models.CharField(max_length=100,verbose_name='备注')

    def __str__(self):
        return self.pro_name

    class Meta:
        verbose_name ='项目信息'
        verbose_name_plural= verbose_name


class Module(models.Model):
    mod_id = models.AutoField(primary_key=True,verbose_name='序号')
    Project = models.ForeignKey(Project, on_delete=models.CASCADE,verbose_name="项目名")
    mod_name= models.CharField(max_length=50,verbose_name='名称')
    mod_code = models.CharField(max_length=50,verbose_name='编码') 
    mod_status = models.BooleanField(default=True,verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    owner = models.ForeignKey('auth.User', related_name='mod', on_delete=models.CASCADE,verbose_name='创建人')
    update_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    remake = models.CharField(max_length=100,verbose_name='备注')   


    def __str__(self):
        return self.mod_name

    class Meta:
        verbose_name ='模块信息'
        verbose_name_plural= verbose_name



class Interface(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='序号')
    Module = models.ForeignKey(Module,on_delete=models.CASCADE,verbose_name='模块名称')
    api = models.CharField(max_length=100,verbose_name='接口地址')
    method = models.CharField(max_length=10,verbose_name='请求方式')
    headers = models.CharField(max_length=100,verbose_name='请求头')
    data = models.CharField(max_length=100,verbose_name='数据')
    response = models.CharField(max_length=1000,verbose_name='响应结果')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    owner = models.ForeignKey('auth.User', related_name='mod', on_delete=models.CASCADE,verbose_name='创建人')
    update_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    remake = models.CharField(max_length=100,verbose_name='备注')  

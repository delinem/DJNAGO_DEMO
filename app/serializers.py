from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import Env,Project,Module
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    envs = serializers.PrimaryKeyRelatedField(many=True, queryset=Env.objects.all())
    pros = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    mods = serializers.PrimaryKeyRelatedField(many=True, queryset=Module.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username','email','envs','pros','mods']


class EnvSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Env
        fields=['env_id','env_name','env_address','env_status','create_time','owner','update_time','remake'] 

    def create(self,env_data):
        return Env.objects.create(**env_data)


    def updata(self,instance,env_data):
        initial.env_name = env_data.get('env_name',initial.env_name)
        initial.env_address = env_data.get('env_address',initial.env_address)
        initial.env_status = env_data.get('env_status',initial.env_status)
        initial.update_time = env_data.get('update_time',initial.update_time)
        initial.remake = env_data.get('remake',initial.remake)
        initial.save()
        return initial

    


class ProjectSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model= Project
        fields ="__all__"

    def create(self,pro_data):
        return Project.objects.create(**pro_data)



class ModuleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    pro_name = serializers.ReadOnlyField(source='pro_name')

    class Meta:
        model= Module
        fields ="__all__"

    def create(self,mod_data):
        return Project.objects.create(**mod_data)


# class EnvSerializer(serializers.Serializer):

#     env_id = models.AutoField(primary_key=True,verbose_name='序号')
#     env_name = models.CharField(max_length=20,verbose_name='名称')
#     env_address = models.CharField(max_length=100,verbose_name='地址')
#     env_status = models.BooleanField(default=True,verbose_name='状态')
#     create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
#     update_time = models.DateTimeField(auto_now=True,verbose_name='创建时间')
#     remake = models.CharField(max_length=100,verbose_name='备注')


#     def create(self,env_data):
#         return Env.objects.create(**env_data)


#     def updata(self,instance,env_data):
#         initial.env_name = env_data.get('env_name',initial.env_name)
#         initial.env_address = env_data.get('env_address',initial.env_address)
#         initial.env_status = env_data.get('env_status',initial.env_status)
#         initial.update_time = env_data.get('update_time',initial.update_time)
#         initial.remake = env_data.get('remake',initial.remake)
#         initial.save()
#         return initial



# class UserSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Group
#         fields = ('url', 'name')
from django.contrib.auth.models import User
from rest_framework import viewsets,permissions,mixins
from rest_framework.views import APIView
from app.models import Env,Project,Module
from app.serializers import EnvSerializer,UserSerializer,ProjectSerializer,ModuleSerializer
from rest_framework import generics
from app.permissions import IsAuthorOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'envs': reverse('env-list', request=request, format=format)
    })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EnvList(generics.ListCreateAPIView):

    queryset = Env.objects.all()
    serializer_class = EnvSerializer
    permission_classes =(permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EnvDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Env.objects.all()
    serializer_class = EnvSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes =(permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class= ProjectSerializer



class ModuleList(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes =(permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(pro_name =self.request.Project,owner=self.request.user)

class ModuleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class= ModuleSerializer


# class EnvView(APIView):

#     def get_object(self, pk):
#         try:
#             return Env.objects.get(pk=pk)
#         except Env.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         env = self.get_object(pk)
#         serializer = EnvSerializer(env)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         env = self.get_object(pk)
#         serializer = EnvSerializer(env, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         env = self.get_object(pk)
#         env.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API端：允许查看和编辑用户
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
    # """
    # API端：允许查看和编辑组
    # """
    # queryset = Group.objects.all()
    # serializer_class = GroupSerializer
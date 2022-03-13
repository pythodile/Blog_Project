from functools import partial
import imp
from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PostSerializer
from .models import *

class PostView(APIView):
    
    def get(self,request,*args,**kwargs):

        post_id = request.GET.get('post_id',None)
        if post_id:
            data =  Post.objects.filter(post_id =  post_id)
            if data:
                sobj = PostSerializer(data,many = True)
                return Response(sobj.data,status = status.HTTP_200_OK)
            else:
                return Response({'Message':'No such Post Exists'},status = status.HTTP_400_BAD_REQUEST)

        data =  Post.objects.filter(status = 'published')
        sobj = PostSerializer(data,many = True)
        return Response(sobj.data, status =status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        try:
            data = request.data
            sobj =  PostSerializer(data = data)
            if sobj.is_valid():
                sobj.save()
                return Response({'Message':'Post Saved'},status =status.HTTP_200_OK)
            else:
                return Response(sobj.errors, status =  status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message':str(e)}, status =  status.HTTP_400_BAD_REQUEST)

    def put(self,request,*args,**kwargs):
        post_id = request.data.get('post_id',None)
        if not post_id:
            return Response({'Message':'Post ID Needs to be required in order to update'}, status =  status.HTTP_400_BAD_REQUEST)
        
        post = Post.objects.filter(pos = post_id)
        if len(post) == 0:
            return Response({'Message':'Invalid post id'}, status =  status.HTTP_400_BAD_REQUEST)
        
        sobj = PostSerializer(post,data = request.data,partial = True)
        if sobj.is_valid():
            sobj.save()
            return Response({'Message':'Post Updated'},status =status.HTTP_200_OK)
        else:
            return Response(sobj.errors, status =  status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,**kwargs):
        post_id = request.data.get('post_id',None)
        if not post_id:
            return Response({'Message':'Post ID Needs to be required in order to delete'}, status =  status.HTTP_400_BAD_REQUEST)
        
        post = Post.objects.filter(pos = post_id)
        if len(post) == 0:
            return Response({'Message':'Invalid post id'}, status =  status.HTTP_400_BAD_REQUEST)
        
        post.delete()
        return Response({'Message':'Post deleted'},status=status.HTTP_204_NO_CONTENT)

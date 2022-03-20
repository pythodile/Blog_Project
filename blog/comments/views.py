from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CommentSerializer
from .models import *
from django.contrib.auth.models import User

# Create your views here.
class CommentsAPI(APIView):
    
    def get(self,request):
        comment_id = request.GET.get('comment_id',None)
        post_id = request.GET.get('post_id',None)
        if comment_id:
            comment = Comment.objects.filter(comment_id=comment_id).first()
            if comment:
                sobj = CommentSerializer(comment)
                return Response(sobj.data,status = status.HTTP_200_OK)
            else:
                return Response({'Message':'No such Comment Exists'},status = status.HTTP_400_BAD_REQUEST)
            
        data =  Comment.objects.filter(post = post_id)
        sobj = CommentSerializer(data,many = True)
        return Response(sobj.data, status =status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        try:
            data = request.data.copy()

            try:
                
                user =  User.objects.get(username=data.get('created_by'))
                data['created_by'] = user.id
            except Exception as e:
                 return Response({'Message':'User does not exists'}, status =  status.HTTP_400_BAD_REQUEST)

            sobj =  CommentSerializer(data = data)
            if sobj.is_valid():
                sobj.save()
                return Response({'Message':'Comment Saved'},status =status.HTTP_200_OK)
            else:
                return Response(sobj.errors, status =  status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message':str(e)}, status =  status.HTTP_400_BAD_REQUEST)

    def put(self,request,*args,**kwargs):
        comment_id = request.data.get('comment_id',None)
        if not comment_id:
            return Response({'Message':'Comment ID Needs to be required in order to update'}, status =  status.HTTP_400_BAD_REQUEST)
        
        comments = Comment.objects.filter(comment_id = comment_id)
        if len(comments) == 0:
            return Response({'Message':'Invalid comment id'}, status =  status.HTTP_400_BAD_REQUEST)
        
        sobj = CommentSerializer(comments,data = request.data,partial = True)
        if sobj.is_valid():
            sobj.save()
            return Response({'Message':'Comment Updated'},status =status.HTTP_200_OK)
        else:
            return Response(sobj.errors, status =  status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,*args,**kwargs):
        comment_id = request.data.get('comment_id',None)
        if not comment_id:
            return Response({'Message':'Comment ID Needs to be required in order to delete'}, status =  status.HTTP_400_BAD_REQUEST)
        
        comments = Comment.objects.filter(comment_id = comment_id)
        if len(comments) == 0:
            return Response({'Message':'Invalid post id'}, status =  status.HTTP_400_BAD_REQUEST)
        
        comments.delete()
        return Response({'Message':'Post deleted'},status=status.HTTP_204_NO_CONTENT)

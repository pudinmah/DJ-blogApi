from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.request import Request
from .models import Post
from .serializers import PostSerializer


# Create your views here.


@api_view(['GET'])
def index(request):

    return Response({"Success":"The setup was successfully"})



@api_view(['GET'])
def GetAllPosts(request):
    get_posts = Post.objects.all()
    serializer = PostSerializer(get_posts, many=True)


    return Response(serializer.data)


@api_view(['GET','POST'])
def CreatePost(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success":"The post was successfully created"},status=201)
    else:
        return Response(serializer.errors, status=400)
    

@api_view(['DELETE'])
def DeletePost(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"Success":"The post was successfully deleted"}, status=200)
    except Post.DoesNotExist:
        return Response({"Error":"The post does not exist"},status=404)

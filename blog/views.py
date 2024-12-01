# blog/views.py
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

# 1. GET All Posts
@api_view(['GET'])
@permission_classes([AllowAny]) 
def get_all_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

# 2. GET a Single Post by ID
@api_view(['GET'])
@permission_classes([AllowAny]) 
def get_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PostSerializer(post)
    return Response(serializer.data)

# 3. POST Create a New Post
@api_view(['POST'])
@permission_classes([AllowAny]) 

def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 4. PUT Update an Existing Post
@api_view(['PUT'])
@permission_classes([AllowAny]) 

def update_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 5. DELETE a Post
@api_view(['DELETE'])
@permission_classes([AllowAny]) 

def delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

    post.delete()
    return Response({'detail': 'Post deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

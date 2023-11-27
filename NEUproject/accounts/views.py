from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth.decorators import login_required


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'A user with that username name is already registered'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import CustomUser

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        # Check if authentication is successful
        if user:
            token, _ = Token.objects.get_or_create(user=user)
        
            response_data = {
                'username': user.username,
                'token': token.key,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # If authentication fails
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

    # If the request method is not POST
    return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
# def user_login(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = None

#         if not user:
#             user = authenticate(username=username, password=password)

#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
        
#             response_data = {
#                 'username': user.username,
#                 'token': token.key,
#             }

#         return Response(response_data, status=status.HTTP_200_OK)

#     return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['POST'])
# @login_required(login_url='/api/login/')
# def create_post(request):
#     if request.method == 'POST':
#         title = request.data.get('title')
#         content = request.data.get('content')

#         # Check if content is provided and is valid
#         if title is None or title.strip() == '':
#             return Response({"error": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)
#         if content is None or content.strip() == '':
#             return Response({"error": "Content is required"}, status=status.HTTP_400_BAD_REQUEST)

#         print(title, content)
#         response_data = {"title": title, "content": content}
#         return Response(response_data, status=status.HTTP_200_OK)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Post
from .serializers import PostSerializer

@api_view(['POST'])
def create_post(request):
    if not request.user.is_authenticated:
        return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(author=request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_post(request):
#     if request.method == 'POST':
#         title = request.data.get('title')
#         content = request.data.get('content')

#         # Check if content is provided and is valid
#         if title is None or title.strip() == '':
#             return Response({"error": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)
#         if content is None or content.strip() == '':
#             return Response({"error": "Content is required"}, status=status.HTTP_400_BAD_REQUEST)

#         # Create a new Post instance and save it to the database
#         post = Post(title=title, content=content, author=request.user, created_at=timezone.now())
#         post.save()

#         # Serialize the new post
#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# def create_post(request):
#     # thread = Thread.objects.get(pk=thread_id)怎么判断有没有login
#     if request.method == 'POST':
#         content = request.data.get('content')
#         print(content)
#         # return redirect('thread_detail', pk=thread_id)
#         response_data = {"result": content}
#         return Response(response_data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
@api_view(['GET','POST'])
def get_post_detail(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        comment_data = {
            'content': request.data.get('content'),
            'post_id': post.post_id  
        }

        comment_serializer = CommentSerializer(data=comment_data, context={'request': request})
        if comment_serializer.is_valid():
            comment_serializer.save(author=request.user)  
            return Response(comment_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        comments = Comment.objects.filter(post_id=post_id).order_by('-created_at')
        comment_serializer = CommentSerializer(comments, many=True)

        post_serializer = PostSerializer(post)

        post_data_with_comments = post_serializer.data
        post_data_with_comments['comments'] = comment_serializer.data

        return Response(post_data_with_comments, status=status.HTTP_200_OK)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateparse import parse_datetime
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def thread_list(request):
    # Get query parameters
    # author_name = request.query_params.get('author_name')
    # start_date = request.query_params.get('start_date')
    # end_date = request.query_params.get('end_date')

    # if author_name:
    #     if not Post.objects.filter(author__username=author_name).exists():
    #         return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)
    #     queryset = Post.objects.filter(author__username=author_name)
    # else:
    #     queryset = Post.objects.all()

    # if start_date:
    #     parsed_start_date = parse_datetime(start_date)
    #     if parsed_start_date is None:
    #         return Response({"error": "Invalid start date format"}, status=status.HTTP_400_BAD_REQUEST)
    #     queryset = queryset.filter(created_at__gte=parsed_start_date)

    # if end_date:
    #     parsed_end_date = parse_datetime(end_date)
    #     if parsed_end_date is None:
    #         return Response({"error": "Invalid end date format"}, status=status.HTTP_400_BAD_REQUEST)
    #     queryset = queryset.filter(created_at__lte=parsed_end_date)
    queryset = Post.objects.all().order_by('-created_at')
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


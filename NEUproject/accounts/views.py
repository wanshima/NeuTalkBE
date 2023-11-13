from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth.decorators import login_required
import random


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

@api_view(['POST'])
@login_required(login_url='/api/login/')
def create_post(request):
    if request.method == 'POST':
        content = request.data.get('content')

        # Check if content is provided and is valid
        if content is None or content.strip() == '':
            return Response({"error": "Content is required"}, status=status.HTTP_400_BAD_REQUEST)

        print(content)
        response_data = {"result": content}
        return Response(response_data, status=status.HTTP_200_OK)
        
# def create_post(request):
#     # thread = Thread.objects.get(pk=thread_id)怎么判断有没有login
#     if request.method == 'POST':
#         content = request.data.get('content')
#         print(content)
#         # return redirect('thread_detail', pk=thread_id)
#         response_data = {"result": content}
#         return Response(response_data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
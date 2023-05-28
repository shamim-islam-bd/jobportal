from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignUpSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view, permission_classes



# Create your views here.............

class SignUp(generics.CreateAPIView): 
    queryset = User.objects.all() 
    serializer_class = SignUpSerializer 
    
    def post(self, request, *args, **kwargs): 
        serializer = SignUpSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password']) # making password hash
            serializer.validated_data['username'] = serializer.validated_data['email'] # making username same as email
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserView(APIView):
    # parser_classes = [MultiPartParser]
    
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    # def put(self, request):
        # before update data user must be authenticated.
        permission_classes = [IsAuthenticated]
        
        user = request.user
        data = request.data
        
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.email = data['email']
        user.password = make_password(data['password'])
        
        # upload resume
        resume = request.FILES['resume']
        
        if resume == '':
            return Response({'detail': 'Please upload resume'}, status=status.HTTP_400_BAD_REQUEST)
        if resume:
            user.resume = resume
        
        serializer = UserSerializer(user, many=False)
        
        print("resume: ", serializer.data)
        
        return Response(serializer.data)
        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        permission_classes = [IsAuthenticated]
        user = request.user
        data = request.data

        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.email = data['email']
        user.password = make_password(data['password'])

        # Upload resume
        resume = request.FILES['resume']

        if resume is None:
            return Response({'detail': 'Please upload a resume'}, status=status.HTTP_400_BAD_REQUEST)

        # Save user object
        user.save()

        serializer = UserSerializer(user)
        
        print("resume getting : ", serializer.data['resume'])

        return Response(serializer.data)
    
    
    
    def delete(self, request):
        # before delete user must be authenticated
        permission_classes = [IsAuthenticated]
        
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def currentUser(request):
    user = UserSerializer(request.user)
    return Response(user.data)


    
    

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from rest_framework import status
from  profile_api import serializers

#viewset 
from rest_framework import viewsets

class HelloApiView(APIView):
    '''test API View'''
    serializer_class = serializers.HelloSerializer
    
    
    def get(self,requet,format=None):
        '''Return a list of Api feature '''
        an_Apivew = {
            'use Http methods as A Fucntiona (Get,Post,Put,patch ,delete)',
            'give a most control on your API',
            'Is mapped manual to URL',
        }
        return Response({'message':'hello!', 'an_Apiview':an_Apivew })
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            messaage = f"Hello {name}  HOW ARE YOU " 
            return Response({'message':messaage})
            
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )
    def put(self,request,pk=None):
        
        return Response({'menthod':'PUT'})
    
    
    def patch(self,request,pk=None):
        
        return Response({'menthod':'PATCH'})
    
    
    def delete(self,request,pk=None):
        
        return Response({'menthod':'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    
    def list(self,request):
        a_viewset = [
            'User Action(list,create, update, partial update,retrive )',
            'Autoatically map to url using Routes',
            'Provied more functionality  in less code '
        ] 
        return Response({'message':'hello sajal', 'a_viewset':a_viewset}) 
    
    def create(self,request,format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f" Welcome to API {name}"
            return Response({'message':message})
        else:
            return Response(
                 serializer.errors,
                status = status.HTTP_400_BAD_REQUEST     
            )
        def retrieve(self,request,pk=None):
            return Response({'http_method':'GET'})
        
        def Update(self,request,pk=None):
            return Response({'http_method':'PUT'})
        
        def partial_update(self,request,pk=None):
            return Response({'http_method':'PATCH'})
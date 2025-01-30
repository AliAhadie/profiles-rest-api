from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api.serializers import HelloSerializer


class HelloApiView(APIView):

    serializer_class=HelloSerializer

    def get(self,request):
        an_api=[
            'hello this is a test from api',
            'with purpose of creating rest api app'
        ]
        message='message'
        context={'an_api':an_api,'message':message}
        return Response(context)
    

    def post(self,request):

        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            email=serializer.validated_data.get('email')
            message=f'Hello {name} your email is {email}'
            return Response({'message':message})
         
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None):
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        return Response({'method':'PATCH'}) 
    
    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})
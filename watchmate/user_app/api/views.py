from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSeializer
from rest_framework.response import Response

from rest_framework.authtoken.models   import Token

@api_view(['POST',])
def registration_view(request):
    
    if request.method == 'POST':
        
        serializer = RegistrationSeializer(data=request.data)
        
        data={}
        
        if serializer.is_valid():
            account = serializer.save()
            data['response']="Registration successful"
            data['username']  = account.username
            data['email'] = account.email
            token = Token.objects.get(user= account).key
            data['token'] = token
        else:
            data = serializer.errors
            
        return Response(data)
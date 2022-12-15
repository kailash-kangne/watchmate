from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSeializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model = User
        fields =['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        print("---------------- save function")
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'error':'p1 & p2 should be same'})
        
        if User.objects.filter(email=email,username=username).exists():
            raise serializers.ValidationError({'error':'email already exists'})
        account = User(email = email, username=username)     
        account.set_password(password)
        account.save()
        
        return account
        
        
        
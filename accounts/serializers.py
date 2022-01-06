from os import write
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User
from django.contrib import auth
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.hashers import make_password
import random
from email.message import EmailMessage
import smtplib

class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68,min_length=6,write_only=True)

    class Meta:
        model=User
        fields=['email' , 'username', 'password']

    def validate(self, attrs):
        email= attrs.get('email','')
        username= attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model=User
        fields=['token']

class LoginSerializer(serializers.ModelSerializer):
    id        = serializers.IntegerField(read_only=True)
    email     = serializers.EmailField(max_length=255,min_length=3,read_only=True)
    password  = serializers.CharField(max_length=68, min_length=6,write_only=True)
    username  = serializers.CharField(max_length=255,min_length=3)
    tokens    = serializers.CharField(max_length=68,read_only=True)

    class Meta:
        model=User
        fields=['id','email','username','password','tokens']

    def validate(self, attrs):
        username=attrs.get('username','')
        password=attrs.get('password','')

        user=auth.authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        return{
            'email':user.email,
            'username':user.username,
            'tokens':user.tokens,
            'id':user.id,
        }

class UserDataSetSerializers(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = "__all__"

class UserDataUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','first_name', 'last_name' , 'email' , 'Dob' , 'Phone' , 'Avatar' , 'gender')

        Avatar  = serializers.FileField (required=False)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.Dob = validated_data.get('Dob', instance.Dob)
        instance.Phone = validated_data.get('Phone', instance.Phone)
        instance.email = validated_data.get('email', instance.email)
        instance.Avatar = validated_data.get('Avatar', instance.Avatar)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=68 , write_only=True)
    token    = serializers.CharField(min_length=1, write_only=True)
    uidb64   = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)
        
class UserSerializers(serializers.Serializer):
        email = serializers.EmailField(min_length=2)
        # username = serializers.CharField(min_length=2)          
        class Meta:
            model  = User
            fields = ['email', 'username']

class SetPasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'password' , 'email')

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = make_password(validated_data.get('password', instance.password))
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class MobSerializers(serializers.Serializer):
    email = serializers.EmailField(min_length=2)
    number_auth = serializers.EmailField(min_length=2)
    class Meta:
        model  = User
        fields = ['Number_auth', 'username']

class ResendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['Number_auth', 'username']

    def validate(self, attrs):
        try:
            email = attrs.get('email')

            user = User.objects.get(email=email)
            number =str(random.randint(0, 100000))
            user.Number_auth = number
            user.save()
            EMAIL_ADDRESS  = 'm.mouafaq.alsaed@gmail.com'
            EMAIL_PASSWORD = 'P@$$w0rd2424'
            msg = EmailMessage()
            msg['Subject'] = 'Verify Your Email In BeezAcademy'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = user.email      
            msg.set_content('Return Number To Active Your Account')
            msg.add_alternative("""\
                <!DOCTYPE html>
                <html>
                <head>
                <style>
                .button {
                border: none;
                color: Black;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                }
                .button1 {background-color: #FFFF00;}
                .a {text-align: center;}
                </style>
                </head>
                    <body>
                        <h3>BeezAcademy</h3>
                        <h3>Hi """+user.username+""" Welcome In BeezAcademy</h3>
                        <h4>Plases Enter This Code In Appliction to verify your email</h3>
                        <h4> The Code Is :""" + number + """</h3>
                    </body>
                </html>
            """, subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)
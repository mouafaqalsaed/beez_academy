# from django.views.generic.base import TemplateView
from django import http
from django.shortcuts import render , redirect
from rest_framework import generics, serializers, status , views
from .serializers import RegisterSerializers, EmailVerificationSerializer, LoginSerializer , UserDataUpdateSerializers , UserDataSetSerializers , ResetPasswordEmailRequestSerializer , SetNewPasswordSerializer , UserSerializers , SetPasswordSerializer , MobSerializers , ResendCodeSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.contrib import messages
from drf_yasg import openapi
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from django.shortcuts import redirect
from django.http import HttpResponsePermanentRedirect
import os
import random
from rest_framework.views import APIView
import smtplib
from email.message import EmailMessage
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated 
# Create your views here.

class RegisterView(generics.GenericAPIView):

    serializer_class=RegisterSerializers

    def post(self, request):
        user = request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user=User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token

        current_site=get_current_site(request).domain
        relativeLink=reverse('email-verify')
        EMAIL_ADDRESS  = 'm.mouafaq.alsaed@gmail.com'
        EMAIL_PASSWORD = 'P@$$w0rd2424'
        msg = EmailMessage()
        msg['Subject'] = 'Verify Your Email In BeezAcademy'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = user.email
        absurl='http://'+current_site+relativeLink+"?token="+str(token)        
        msg.set_content('Click Button To Active Your Account')
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
                        <h3>Hi """+user.username+""" Welcome In BeezAcademy</h3>
                        <h3>Plases Enter Button to verify your email</h3>
                        <a class="a" href="""+ absurl +"""><button class="button button1">Click here to activate</button></a>
                    </body>
                </html>
        """, subtype='html')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return Response(user_data ,status=status.HTTP_201_CREATED)

class VerifyEmail(views.APIView):
    serializer_class=EmailVerificationSerializer
    token_param_config=openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description',type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token=request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user=User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified= True
                user.save()
            # return Response({'email' : 'Succesfully activated'}, status=status.HTTP_200_OK)
                messages.success(request, 'Profile details updated.')
            return redirect('http://127.0.0.1:8080/')
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error' : 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error' : 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    def post(self , request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UsersDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDataUpdateSerializers

class GetUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDataSetSerializers

class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))       
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            absurl = 'https://bzacd.com'+ relativeLink
            email_body = 'Hello, \n Use link below to reset your password  \n' + absurl
            data = {'email_body': email_body, 'to_email': user.email,'email_subject': 'Reset your passsword'}
            Util.send_email(data)
            return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        return Response({'error': 'The Email not Found'}, status=status.HTTP_400_BAD_REQUEST)

class PasswordTokenCheckAPI(generics.GenericAPIView):
    # serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)

            # return redirect('http://bzacd.com/' , Response({'success': True , 'message':'Credentials Valid' , 'uidb64':uidb64 , 'token': token}, status=status.HTTP_200_OK))
            return Response({'success': True , 'message':'Credentials Valid' , 'uidb64':uidb64 , 'token': token}, status=status.HTTP_200_OK)
        
        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)

class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)

class test(generics.GenericAPIView):
    serializer_class = UserSerializers
    def post(self , request):
        email = request.data.get('email', '')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            username = user.username
            return Response({'username':username}, status=status.HTTP_200_OK)
        if not User.objects.filter(email=email).exists():
            username = 'null'
            return Response({'username':username}, status=status.HTTP_200_OK)

class ChangePasswordView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = SetPasswordSerializer

class RegisterMob(generics.GenericAPIView):

    serializer_class=RegisterSerializers

    def post(self, request):
        user = request.data
        number =str(random.randint(0, 100000))
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user=User.objects.get(email=user_data['email'])
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

        return Response({'detail':'Please Verify Your Email'} ,status=status.HTTP_201_CREATED)

class RegisterMobVerify(generics.GenericAPIView):
    serializer_class = MobSerializers

    def post(self , request):
        email       = request.data.get('email', '')
        number_auth = request.data.get('number_auth', '')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            Number_auth = user.Number_auth
            if Number_auth==number_auth:
                user.is_verified= True
                user.save()
                return Response({'is_verified' : 'Done'}, status=status.HTTP_200_OK)
            if Number_auth!=number_auth:
                return Response({'is_verified' : 'False'}, status=status.HTTP_400_BAD_REQUEST)
        return Response('Please Check The Entered Data', status=status.HTTP_400_BAD_REQUEST)

class ResendCode(generics.GenericAPIView):
    serializer_class = ResendCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'The code has been resend'}, status=status.HTTP_200_OK)
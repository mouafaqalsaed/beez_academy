from os import name
from django.urls import path
from .views import RegisterView , VerifyEmail , LoginAPIView , UsersDetailAPIView , GetUser , RequestPasswordResetEmail , PasswordTokenCheckAPI , SetNewPasswordAPIView , test , ChangePasswordView , RegisterMob , RegisterMobVerify , ResendCode


urlpatterns = [
    path('register/'                       , RegisterView.as_view(),name='register'),
    path('login/'                          , LoginAPIView.as_view(),name="login"),
    path('email-verify/'                   , VerifyEmail.as_view(),name='email-verify'),
    path('ProfileUpdate/<int:pk>/'         , UsersDetailAPIView.as_view() , name="user-detail"),
    path('Profile/<int:pk>/'               , GetUser.as_view() , name="customer-detail"),
    path('request-reset-email/'            , RequestPasswordResetEmail.as_view(),name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete'         , SetNewPasswordAPIView.as_view(),name='password-reset-complete'),
    path('check-user/'                     , test.as_view() , name='check-user'),
    path('set-password/<int:pk>/'          , ChangePasswordView.as_view() , name='set-password'),
    path('register-mob/'                   , RegisterMob.as_view() , name='register-mob'),
    path('register-mob-verify/'            , RegisterMobVerify.as_view() , name='register-mob-verify'),
    path('ResendCode/'                     , ResendCode.as_view() , name='ResendCode'),
]
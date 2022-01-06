from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    justname = filename.split('.')[0]
    filename = "%s.%s" % (justname, ext)
    return os.path.join('static/images/profile/', filename)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password ):
        if password is None:
            raise TypeError('Password should not be none')

        user=self.create_user(username , email,password )
        user.is_superuser = True
        user.is_staff=True
        user.save()
        return user

AUTH_PROVIDERS = {'facebook': 'facebook','google': 'google', 'email': 'email'}

class User(AbstractBaseUser,PermissionsMixin):
    username      = models.CharField(max_length=255, unique=True , db_index=True)
    first_name    = models.CharField(max_length=30, blank=True)
    last_name     = models.CharField(max_length=150, blank=True)
    email         = models.EmailField(max_length=255, unique=True , db_index=True)
    is_verified   = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    is_staff      = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    Dob           = models.DateField(null=True, blank=True)
    Avatar        = models.FileField(default="static/images/profile/person.png", upload_to=get_file_path,blank=True, null=True)
    Phone         = models.CharField(max_length=190 , null=True ,blank=True)
    Number_auth   = models.CharField(default="1" , max_length=190 , null=True , blank=True)
    auth_provider = models.CharField(max_length=255 , blank=False , null=False , default=AUTH_PROVIDERS.get('email'))
    GENDER        = (('Male','Male'),('Female','Female'))
    gender        = models.CharField(max_length=190,null=True,choices=GENDER)
    TYPE_USER     = (('is_parents','Is Parents'),('is_student','Is Student'),('is_teacher ','Is Teacher'))
    type_user     = models.CharField(max_length=190,null=True,choices=TYPE_USER)
    LIVE          = (('Afghanistan','Afghanistan'),('Aland Islands','Aland Islands'),('Albania','Albania'),('Algeria','Algeria'),('American Samoa','American Samoa'),('Andorra','Andorra'),('Angola','Angola'),('Anguilla','Anguilla'),('Antarctica','Antarctica'),('Antigua and Barbuda','Antigua and Barbuda'),('Argentina','Argentina'),('Armenia','Armenia'),('Aruba','Aruba'),('Australia','Australia'),('Austria','Austria'),('Azerbaijan','Azerbaijan'),('Bahamas','Bahamas'),('Bahrain','Bahrain'),('Bangladesh','Bangladesh'),('Barbados','Barbados'),('Belarus','Belarus'),('Belgium','Belgium'),('Belize','Belize'),('Benin','Benin'),('Bermuda','Bermuda'),('Bhutan','Bhutan'),('Bolivia','Bolivia'),('Bosnia and Herzegovina','Bosnia and Herzegovina'),('Botswana','Botswana'),('Bouvet Island','Bouvet Island'),('Brazil','Brazil'),('British Indian Ocean Territory','British Indian Ocean Territory'),('Brunei Darussalam','Brunei Darussalam'),('Bulgaria','Bulgaria'),('Burkina Faso','Burkina Faso'),('Burundi','Burundi'),('Cambodia','Cambodia'),('Cameroon','Cameroon'),('Canada','Canada'),('Cape Verde','Cape Verde'),('Cayman Islands','Cayman Islands'),('Central African Republic','Central African Republic'),('Chad','Chad'),('Chile','Chile'),('China','China'),('Christmas Island','Christmas Island'),('Cocos (Keeling) Islands','Cocos (Keeling) Islands'),('Colombia','Colombia'),('Comoros','Comoros'),('Congo','Congo'),('Cook Islands','Cook Islands'),('Costa Rica','Costa Rica'),('Croatia','Croatia'),('Cuba','Cuba'),('Cyprus','Cyprus'),('Denmark','Denmark'),('Djibouti','Djibouti'),('Dominica','Dominica'),('Ecuador','Ecuador'),('Egypt','Egypt'),('El Salvador','El Salvador'),('Eritrea','Eritrea'),('Estonia','Estonia'),('Ethiopia','Ethiopia'),('Faroe Islands','Faroe Islands'),('Fiji','Fiji'),('Finland','Finland'),('France','France'),('Gabon','Gabon'),('Gambia','Gambia'),('Georgia','Georgia'),('Germany','Germany'),('Ghana','Ghana'),('Gibraltar','Gibraltar'),('Guam','Guam'),('Guinea','Guinea'),('Guyana','Guyana'),('Iceland','Iceland'),('India','India'),('Indonesia','Indonesia'),('Iran','Iran'),('Iraq','Iraq'),('Ireland','Ireland'),('Israel','Israel'),('Italy','Italy'),('Jamaica','Jamaica'),('Japan','Japan'),('Jersey','Jersey'),('Jordan','Jordan'),('Kazakhstan','Kazakhstan'),('Kenya','Kenya'),('Kiribati','Kiribati'),('Korea','Korea'),('Kuwait','Kuwait'),('Kyrgyzstan','Kyrgyzstan'),('Latvia','Latvia'),('Lebanon','Lebanon'),('Liberia','Liberia'),('Libyan Arab Jamahiriya','Libyan Arab Jamahiriya'),('Macao','Macao'),('Malawi','Malawi'),('Malaysia','Malaysia'),('Maldives','Maldives'),('Mali','Mali'),('Malta','Malta'),('Mexico','Mexico'),('Morocco','Morocco'),('Mozambique','Mozambique'),('Nigeria','Nigeria'),('Northern','Northern'),('Oman','Oman'),('Pakistan','Pakistan'),('Paraguay','Paraguay'),('Peru','Peru'),('Philippines','Philippines'),('Poland','Poland'),('Portugal','Portugal'),('Qatar','Qatar'),('Romania','Romania'),('Russian','Russian'),('Rwanda','Rwanda'),('Samoa','Samoa'),('San Marino','San Marino'),('Saudi Arabia','Saudi Arabia'),('Senegal','Senegal'),('Serbia','Serbia'),('South Africa','South Africa'),('Spain','Spain'),('Sudan','Sudan'),('Swaziland','Swaziland'),('Syrian Arab Republic','Syrian Arab Republic'),('Taiwan','Taiwan'),('Togo','Togo'),('Tonga','Tonga'),('Tunisia','Tunisia'),('Turkey','Turkey'),('Turkmenistan','Turkmenistan'),('Uganda','Uganda'),('Ukraine','Ukraine'),('United Arab Emirates','United Arab Emirates'),('United Kingdom','United Kingdom'),('United States','United States'),('Uruguay','Uruguay'),('Uzbekistan','Uzbekistan'),('Vanuatu','Vanuatu'),('Venezuela','Venezuela'),('Viet Nam','Viet Nam'),('Virgin Islands','Virgin Islands'),('Wallis and Futuna','Wallis and Futuna'),('Western Sahara','Western Sahara'),('Yemen','Yemen'),('Zambia','Zambia'),('Zimbabwe','Zimbabwe'))
    live          = models.CharField(max_length=190,null=True,choices=LIVE)
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username
    
    def tokens(self):
        refresh=RefreshToken.for_user(self)
        return str(refresh.access_token)

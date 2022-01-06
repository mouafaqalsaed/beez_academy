#from backend.Beezaccs.models import Classes
from datetime import datetime
from os import read
from django.db import models
from django.db.models.fields import files
from django.utils.timesince import timesince
from rest_framework import serializers
from Beezaccs.models import Exercises , Categories , ContactUs , Kin_CategoryType , Level , Classes , Kin_CategoriesClass , Kin_ExercisesOnline , Topic , Sub_Topic

# Serializers To Return All Exercises
class ExercisesSerializers(serializers.ModelSerializer):
    class Meta:
        model    = Exercises
        fields = "__all__"

# Serializers To Return All Categories
class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model    = Categories
        fields = "__all__"        

# Serializers To Return Exercises To Choose Categories
class CategoriesExercisesSerializers(serializers.ModelSerializer):
    exercises = ExercisesSerializers(many= True , read_only=True , )
    class Meta:
        model  = Categories
        fields = "__all__"
        
# Serializers To return All ContactUs
class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model    = ContactUs
        fields = "__all__" 
        
# Serializers To Return All CategoriesType
class CategoryTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model    = Kin_CategoryType
        fields = "__all__" 

# PHASE02
# PHASE02-->Kindergarten
# Serializers To return All Level
class LevelSerializers(serializers.ModelSerializer):
    class Meta:
        model    = Level
        fields = "__all__"

# Serializers To Return Categories To Choose LevelKg
class CategoryLevelKgSerializers(serializers.ModelSerializer):
    class Meta:
        model    = Kin_CategoryType
        fields = "__all__" 

# Serializers To Return Categories To Choose LevelKg
class CategoryKgSerializers(serializers.ModelSerializer):
    class Meta:
        model    = Kin_CategoriesClass
        fields = "__all__" 

# Serializers To Return All Exercises
class ClassesSerializers(serializers.ModelSerializer):
    class Meta:
        model    = Classes
        fields = "__all__"

# Serializers To Return classes To Choose Level
class LevelClassesSerializers(serializers.ModelSerializer):
    classes = ClassesSerializers(many= True , read_only=True , )
    class Meta:
        model  = Level
        fields = "__all__"

# Serializers To Return All Topic To Choose categories To Choose classes
class Kin_ExercisesOnlineSerializers(serializers.Serializer):
    # topic = serializers.CharField(min_length=0)
    categories = serializers.CharField(min_length=0)
    classes = serializers.CharField(min_length=0)
    class Meta:
        model    = Kin_ExercisesOnline
        fields = "__all__"
        depth = 1

# Serializers To Return All Topic
class TopicSerializers(serializers.ModelSerializer):
    class Meta:
        model    = Topic
        fields = "__all__"

# Serializers To Return All Topic To Choose categories To Choose classes
# class ExercisesTopicSerializers(serializers.ModelSerializer):
#     class Meta:
#         model    = Topic
#         fields = ["Topic"]

# Serializers To Return All Topic
# class ExercisesSubTopicSerializers(serializers.ModelSerializer):
#     class Meta:
#         model    = Kin_ExercisesOnline
#         fields = ["sub_topic"]
#         depth = 1

#Serializers To Return All Topic To Choose categories To Choose classes
class Kin_ExercisescSerializers(serializers.ModelSerializer):
    class Meta:
        model    = Kin_ExercisesOnline
        fields = "__all__"

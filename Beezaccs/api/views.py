import json
import re
import urllib
from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse , HttpResponse
from rest_framework.utils import serializer_helpers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from django.db.models.query import QuerySet
from rest_framework.views import APIView
from django.views.generic import ListView
from django.core.serializers import serialize
from django.core import serializers
from django.http import JsonResponse
from datetime import datetime , timedelta
from datetime import date
from django.utils import timezone
from accounts.models import User 
from Beezaccs.models import Exercises , Categories , ContactUs , StudentSchoole , Post , StudentAssignment , Like , Comment , ExersiseType , is_True , Procedure , TopicType , DurationTime , Section
from Beezaccs.api.serializers import  ExercisesSerializers , CategoriesSerializers , CategoriesExercisesSerializers , ContactUsSerializers , CategoryTypeSerializers , LevelSerializers , CategoryLevelKgSerializers , CategoryKgSerializers
from Beezaccs.models import Level , Kin_CategoryType , Kin_CategoriesClass  , Kin_ExercisesOnline , Kin_LinkExercises , Classes , Topic , Sub_Topic
from Beezaccs.models import Pr_Classes , Pr_Subject , Pr_Uint , Pr_Topic , Pr_Summary , Pr_ExercisesOnline , Pr_Link_Exercises , Pr_Subject , Pr_ExersiseType , Pr_is_True
from Beezaccs.models import Mid_Subject , Mid_Classes , Mid_Uint , Mid_Topic , Mid_ExersiseType , Mid_is_True , Mid_ExercisesOnline
# from Beezaccs.models import ChatSession , ChatSessionMessage , deserialize_user
from django.contrib.auth import get_user_model
# from notifications.signals import notify
# PHASE01

# Exercises List API
class ExercisesListCreateAPIView(generics.ListCreateAPIView):
        queryset = Exercises.objects.all()
        serializer_class = ExercisesSerializers

# Exercises Detail API
class ExercisesDetailUpdateAndDeletedAPIView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Exercises.objects.all()
        serializer_class = ExercisesSerializers

# Categories List API
class CategoriesListCraeteAPIView(generics.ListCreateAPIView):
        queryset = Categories.objects.all()
        serializer_class = CategoriesSerializers

# Categories Detail API
class CategoriesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesExercisesSerializers
    
# ContactUsCreate API
class ContactUsCreate(generics.ListCreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializers

# CategoryTypeSerializers API
class CategoryTypeAPIView(generics.ListCreateAPIView):
        queryset = Kin_CategoryType.objects.all()
        serializer_class = CategoryTypeSerializers

# PHASE02
# API To Return Dashborad To Mr.Mohamed.
class PrivateMDashborad (generics.GenericAPIView):
        def get(self , request):
                json_res      = []
                today           = date.today()
                yesterday       = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
                sql01           = Kin_ExercisesOnline.objects.filter().count()
                sql02           = Pr_ExercisesOnline.objects.filter().count()
                sql03           = Topic.objects.filter().count()
                sql04           = Pr_Uint.objects.filter().count()
                sql05           = Sub_Topic.objects.filter().count()
                sql06           = Pr_Topic.objects.filter().count()
                sql07           = Pr_ExercisesOnline.objects.filter(classes_id=1).count()
                sql08           = Pr_ExercisesOnline.objects.filter(classes_id=2).count()
                sql09           = Pr_ExercisesOnline.objects.filter(classes_id=3).count()
                sql10           = Pr_Summary.objects.filter().count()
                sql11           = Kin_ExercisesOnline.objects.filter(created_at__gt=today).count()
                sql12           = Kin_ExercisesOnline.objects.filter(created_at__gt=yesterday).count()-sql11
                sql13           = Pr_ExercisesOnline.objects.filter(created_at__gt=today,classes_id=1).count()
                sql14           = Pr_ExercisesOnline.objects.filter(created_at__gt=yesterday,classes_id=1).count()-sql13
                sql15           = Pr_ExercisesOnline.objects.filter(created_at__gt=today,classes_id=2).count()
                sql16           = Pr_ExercisesOnline.objects.filter(created_at__gt=yesterday,classes_id=2).count()-sql15
                sql17           = Pr_ExercisesOnline.objects.filter(created_at__gt=today,classes_id=3).count()
                sql18           = Pr_ExercisesOnline.objects.filter(created_at__gt=yesterday,classes_id=3).count()-sql17
                return Response({"Dashborad":'Welcome To BeezAcademy' , 'Total_Exersise_In_Academy':sql01+sql02 ,'Total_Unit_In_Academy':sql03+sql04,'Total_Topic_In_Academy':sql05+sql06,'Total_Summary_In_Academy':sql10, 'Total_Exersise_In_Kindergarten_Level':sql01, 'Total_Exersise_In_Kindergarten_Level_Today':sql11, 'Total_Exersise_In_Kindergarten_Level_Yesterday':sql12 ,'Total_Exersise_In_Grade1':sql07, 'Total_Exersise_In_Grade1_Today':sql13, 'Total_Exersise_In_Grade1_Yesterday':sql14,'Total_Exersise_In_Grade2':sql08, 'Total_Exersise_In_Grade2_Today':sql15, 'Total_Exersise_In_Grade2_Yesterday':sql16,'Total_Exersise_In_Grade3':sql09, 'Total_Exersise_In_Grade3_Today':sql17, 'Total_Exersise_In_Grade3_Yesterday':sql18})
# PHASE02-->Kindergarten
# API To Return Levels List API
class LevelsAPIView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializers

# API To Return Type Level Kindergarten Detail API
class GetCategoriesToKgLevel(generics.ListCreateAPIView):
        queryset = Kin_CategoryType.objects.all()
        serializer_class = CategoryLevelKgSerializers

# API To Return Subjects To Specific Class Level Kindergarten List API
class kgsubjects(generics.GenericAPIView):
        def get(self , request):
                json_res      = []
                sql           = "SELECT id , category , created_at , updated_at , alternative_image FROM Beezaccs_kin_categoriesclass order by id"
                IDClass       = Kin_CategoriesClass.objects.raw(sql)
                for record in IDClass:
                        json_obj  = dict(ID = record.id , Subject=record.category, created_at=record.created_at , updated_at=record.updated_at , alternative_image=record.alternative_image)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Return Classes Level Kindergarten Detail API
class kgClasses(generics.GenericAPIView):
        def get(self , request):
                json_res      = []
                sql           = "select DISTINCT Beezaccs_classes.id , Beezaccs_classes.classes , Beezaccs_classes.alternative_image from Beezaccs_classes order by Beezaccs_classes.id"
                IDClass       = Classes.objects.raw(sql)
                for record in IDClass:
                        json_obj  = dict(ID = record.id , Class=record.classes)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Return List Topic Related To Custom class and Custom categories
class ExercisesTopic(generics.GenericAPIView):
    def get(self , request , ClassName , SubjectName):
        if Classes.objects.filter(classes=ClassName).exists():
                if Kin_CategoriesClass.objects.filter(category=SubjectName).exists():
                        Subject = Kin_CategoriesClass.objects.get(category=SubjectName)
                        SubjectId = Subject.id
                        Class = Classes.objects.get(classes=ClassName)
                        ClassId = Class.id
                        json_res          = []
                        sql               = "select DISTINCT Beezaccs_topic.id , Beezaccs_topic.Topic from Beezaccs_topic inner join Beezaccs_kin_exercisesonline on Beezaccs_topic.id = Beezaccs_kin_exercisesonline.topic_id where classes_id=" + str(ClassId) + " and categories_id=" + str(SubjectId) + " order by Beezaccs_topic.id"
                        Exersise_ID       = Kin_ExercisesOnline.objects.raw(sql)
                        for record in Exersise_ID: 
                                json_obj  = dict(ID = record.id ,Unit = record.Topic)
                                json_res.append([json_obj])
                        return Response({'Data':json_res})

# API To Return List SubTopic Related To Custom Topic
class ExercisesSubTopic(generics.GenericAPIView):
    def get(self , request , TobicName):
        if Topic.objects.filter(Topic=TobicName).exists():
                        Topics  = Topic.objects.get(Topic=TobicName)
                        TopicId = Topics.id
                        json_res      = []
                        sql           = "select DISTINCT Beezaccs_sub_topic.id , Beezaccs_sub_topic.Sub_Topic from Beezaccs_sub_topic inner join Beezaccs_kin_exercisesonline on Beezaccs_sub_topic.id = Beezaccs_kin_exercisesonline.sub_topic_id where topic_id=" + str(TopicId) + " order by Beezaccs_sub_topic.Sub_Topic"
                        Exersise_ID   = Kin_ExercisesOnline.objects.raw(sql)
                        for record in Exersise_ID: 
                                json_obj  = dict(ID = record.id , Topic = record.Sub_Topic)
                                json_res.append([json_obj])
                        return Response({'Data':json_res})

# API To Return List Topic And SubTopic Related To Custom class and Custom categories
class ExercisesTopicSubTopic(generics.GenericAPIView):  
    def get(self , request , ClassName , SubjectName):
        if Classes.objects.filter(classes=ClassName).exists():
                if Kin_CategoriesClass.objects.filter(category=SubjectName).exists():
                        sub = Kin_CategoriesClass.objects.get(category=SubjectName)
                        sub_id = sub.id
                        cl = Classes.objects.get(classes=ClassName)
                        cl_id = cl.id
                        json_res      = []
                        sql           = "select DISTINCT Beezaccs_kin_exercisesonline.sub_topic_id , Beezaccs_sub_topic.Sub_Topic , Beezaccs_topic.id , Beezaccs_topic.Topic from Beezaccs_kin_exercisesonline inner join Beezaccs_sub_topic on Beezaccs_sub_topic.id = Beezaccs_kin_exercisesonline.sub_topic_id inner join Beezaccs_topic on Beezaccs_topic.id = Beezaccs_kin_exercisesonline.topic_id where classes_id=" + str(cl_id) + " and categories_id=" + str(sub_id) + " order by Beezaccs_topic.id"
                        Exersise_ID   = Kin_ExercisesOnline.objects.raw(sql)
                        for record in Exersise_ID: 
                                json_obj  = dict(IDUnit = record.id , Unit = record.Topic , IDTopic = record.sub_topic_id , Topic = record.Sub_Topic)
                                json_res.append([json_obj])
                        return Response({'Data':json_res})

# API To Return List Exercises Related To Custom class and Custom categories and Custom Topic and Custom SubTopic
class ExercisesAPIView (generics.GenericAPIView):
        def get(self , request , ClassName , SubjectName , TopicName , SubTopicName):
                if Classes.objects.filter(classes=ClassName).exists():
                        if Kin_CategoriesClass.objects.filter(category=SubjectName).exists():
                                if Topic.objects.filter(Topic=TopicName).exists():
                                        if Sub_Topic.objects.filter(Sub_Topic=SubTopicName).exists():
                                                cl = Classes.objects.get(classes=ClassName)
                                                cl_id = cl.id
                                                sub = Kin_CategoriesClass.objects.get(category=SubjectName)
                                                sub_id = sub.id
                                                top = Topic.objects.get(Topic=TopicName)
                                                topic_id = top.id
                                                topsub = Sub_Topic.objects.get(Sub_Topic=SubTopicName)
                                                topicsub_id = topsub.id
                                                json_res      = []
                                                sql           = "select Beezaccs_kin_exercisesonline.id,Beezaccs_kin_exercisesonline.exercise,Beezaccs_kin_exercisesonline.is_Done,Beezaccs_kin_exercisesonline.is_Free,Beezaccs_kin_exercisesonline.A,Beezaccs_kin_exercisesonline.B,Beezaccs_kin_exercisesonline.C,Beezaccs_kin_exercisesonline.D,Beezaccs_kin_exercisesonline.A_Image,Beezaccs_kin_exercisesonline.B_Image,Beezaccs_kin_exercisesonline.C_Image,Beezaccs_kin_exercisesonline.D_Image,Beezaccs_kin_exercisesonline.alternative_A_Image,Beezaccs_kin_exercisesonline.alternative_B_Image,Beezaccs_kin_exercisesonline.alternative_C_Image,Beezaccs_kin_exercisesonline.alternative_D_Image,Beezaccs_kin_exercisesonline.created_at,Beezaccs_kin_exercisesonline.updated_at,Beezaccs_kin_exercisesonline.File,Beezaccs_kin_exercisesonline.alternative_image,Beezaccs_kin_exercisesonline.categories_id,Beezaccs_kin_exercisesonline.classes_id,Beezaccs_kin_exercisesonline.exercisetypy_id,Beezaccs_kin_exercisesonline.sub_topic_id,Beezaccs_kin_exercisesonline.topic_id,Beezaccs_is_true.istrue FROM Beezaccs_kin_exercisesonline inner join Beezaccs_is_true on Beezaccs_kin_exercisesonline.is_True_id=Beezaccs_is_true.id where sub_topic_id=" + str(topicsub_id) + " and topic_id =" + str(topic_id) + " and classes_id=" + str(cl_id) + " and categories_id=" + str(sub_id) + " ORDER BY Beezaccs_kin_exercisesonline.id"
                                                Exersise_Total= Kin_ExercisesOnline.objects.filter(sub_topic_id=topicsub_id,topic_id=topic_id, categories_id=sub_id,classes_id=cl_id).count()
                                                Exersise_ID   = Kin_ExercisesOnline.objects.raw(sql)
                                                URLROOT       = 'https://publicws.bzacd.com'
                                                for record in Exersise_ID:
                                                        json_obj  = dict(IDExercises = record.id , Exercise = record.exercise , IsDone = record.is_Done , IsFree = record.is_Free , A = record.A , B = record.B , C = record.C , D = record.D , A_Image = URLROOT+record.A_Image.url , B_Image = URLROOT+record.B_Image.url  , C_Image = URLROOT+record.C_Image.url , D_Image = URLROOT+record.D_Image.url , alternative_A_Image = record.alternative_A_Image , alternative_B_Image = record.alternative_B_Image , alternative_C_Image = record.alternative_C_Image , alternative_D_Image = record.alternative_D_Image , created_at =  record.created_at , updated_at = record.updated_at , File = URLROOT+record.File.url , Image = URLROOT+record.image.url,alternative_image = record.alternative_image, Categories = record.categories_id , Classes = record.classes_id , ExerciseType = record.exercisetypy_id  , Level = record.level_id , SubTopic = record.sub_topic_id , Topic = record.topic_id)
                                                        json_res.append([json_obj])
                                                return Response({'Count':Exersise_Total , 'Data':json_res})

# API To Return Custom Exercise
class ExerciseAPIView (generics.GenericAPIView):
        def get(self , request , ID):
                json_res      = []
                sql           = "select * from Beezaccs_kin_exercisesonline where id="+ID
                Exersise_ID   = Kin_ExercisesOnline.objects.raw(sql)
                URLROOT       = 'https://publicws.bzacd.com'
                for record in Exersise_ID:
                        json_obj  = dict(IDExercises = record.id , Exercise = record.exercise , IsDone = record.is_Done , IsFree = record.is_Free , A = record.A , B = record.B , C = record.C , D = record.D , A_Image = URLROOT+record.A_Image.url , B_Image = URLROOT+record.B_Image.url  , C_Image = URLROOT+record.C_Image.url , D_Image = URLROOT+record.D_Image.url , alternative_A_Image = record.alternative_A_Image , alternative_B_Image = record.alternative_B_Image , alternative_C_Image = record.alternative_C_Image , alternative_D_Image = record.alternative_D_Image , created_at =  record.created_at , updated_at = record.updated_at , File = URLROOT+record.File.url , Image = URLROOT+record.image.url,alternative_image = record.alternative_image, Categories = record.categories_id , Classes = record.classes_id , ExerciseType = record.exercisetypy_id , Level = record.level_id , SubTopic = record.sub_topic_id , Topic = record.topic_id)
                        json_res.append([json_obj])
                return Response({'Data':json_res})    

# API To Return List True Answer Related To Custom class and Custom categories and Custom Topic and Custom SubTopic
class AnswerExercisesAPIView (generics.GenericAPIView):
        def get(self , request , ClassName , SubjectName , TopicName , SubTopicName):
                if Classes.objects.filter(classes=ClassName).exists():
                        if Kin_CategoriesClass.objects.filter(category=SubjectName).exists():
                                if Topic.objects.filter(Topic=TopicName).exists():
                                        if Sub_Topic.objects.filter(Sub_Topic=SubTopicName).exists():
                                                cl = Classes.objects.get(classes=ClassName)
                                                cl_id = cl.id
                                                sub = Kin_CategoriesClass.objects.get(category=SubjectName)
                                                sub_id = sub.id
                                                top = Topic.objects.get(Topic=TopicName)
                                                topic_id = top.id
                                                topsub = Sub_Topic.objects.get(Sub_Topic=SubTopicName)
                                                topicsub_id = topsub.id
                                                json_res      = []
                                                sql           = "select Beezaccs_kin_exercisesonline.id , Beezaccs_is_true.istrue  from Beezaccs_kin_exercisesonline inner join Beezaccs_is_true on Beezaccs_kin_exercisesonline.is_True_id=Beezaccs_is_true.id where sub_topic_id=" + str(topicsub_id) + " and topic_id =" + str(topic_id) + " and classes_id=" + str(cl_id) + " and categories_id=" + str(sub_id) + " order by Beezaccs_kin_exercisesonline.id"
                                                sqlTotal      = Kin_ExercisesOnline.objects.filter(sub_topic_id=topicsub_id,topic_id=topic_id, categories_id=sub_id,classes_id=cl_id).count()
                                                Exersise_ID   = Kin_ExercisesOnline.objects.raw(sql)
                                                for record in Exersise_ID:
                                                        json_obj  = dict(IDExercises = record.id , TrueAnswer = record.istrue)
                                                        json_res.append([json_obj])
                                                return Response({'Count':sqlTotal , 'Data':json_res})

# API To Return True Answer Related To Custom Exercise
class AnswerExerciseAPIView (generics.GenericAPIView):
        def get(self , request , ID):
                json_res      = []
                sql           = "select Beezaccs_kin_exercisesonline.id , Beezaccs_is_true.istrue from Beezaccs_kin_exercisesonline inner join Beezaccs_is_true on Beezaccs_kin_exercisesonline.is_True_id=Beezaccs_is_true.id where Beezaccs_kin_exercisesonline.id="+ID
                Exersise_ID   = Kin_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        json_obj  = dict(TrueAnswer = record.istrue)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Return Result About Answer User
class ResultAnswerAPIView (generics.GenericAPIView):
        def get(self , request , ID , Answer):
                json_res      = []
                sql           = "select Beezaccs_kin_exercisesonline.id , Beezaccs_is_true.istrue from Beezaccs_kin_exercisesonline inner join Beezaccs_is_true on Beezaccs_kin_exercisesonline.is_True_id=Beezaccs_is_true.id where Beezaccs_kin_exercisesonline.id="+ID
                Exersise_ID   = Kin_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.istrue==Answer):
                                return Response({'Data':'True'})
                        else:
                                return Response({'Data':'False'})

# API To Link Exercise To User
class InsertExerciseAPIView (generics.GenericAPIView):
        def get(self , request , ID_user , ID_exercise , Time , Answer , TrueAnswer):
                user = User.objects.filter(id=ID_user)
                for record in user:
                        IdUser  = record.id
                Kin_LinkExercises.objects.create(user=IdUser,exercise=ID_exercise,duration_Time=Time,answer=Answer,true_answer=TrueAnswer)
                return Response({'Data':'Successfully Added'})

# PHASE02
# PHASE02-->Primary
# API To Return Classes Level Primary Detail API
class prClasses(generics.GenericAPIView):
        def get(self , request):
                json_res      = []
                sql           = "select DISTINCT Beezaccs_pr_classes.id , Beezaccs_pr_classes.classes from Beezaccs_pr_classes order by Beezaccs_pr_classes.id"
                IDClass       = Pr_Classes.objects.raw(sql)
                for record in IDClass:
                        json_obj  = dict(ID = record.id , Class=record.classes)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Return Subjects To Specific Class Level Kindergarten List API
class prSubjects(generics.GenericAPIView):
        def get(self , request , ClassName):
                if Pr_Classes.objects.filter(classes=ClassName).exists():
                        Class = Pr_Classes.objects.get(classes=ClassName)
                        ClassId = Class.id
                        json_res      = []
                        sql           = "select DISTINCT Beezaccs_pr_subject.id , Beezaccs_pr_subject.subject , Beezaccs_pr_subject.created_at , Beezaccs_pr_subject.updated_at from Beezaccs_pr_exercisesonline inner join Beezaccs_pr_subject on Beezaccs_pr_exercisesonline.subject_id = Beezaccs_pr_subject.id WHERE classes_id=" + str(ClassId)
                        IDClass       = Pr_Subject.objects.raw(sql)
                        for record in IDClass:
                                json_obj  = dict(ID = record.id , Subject=record.subject , created_at=record.created_at , updated_at=record.updated_at)
                                json_res.append([json_obj])
                        return Response({'Data':json_res})

# API To Return List Uints Related To Custom class and Custom subjects
class prUints(generics.GenericAPIView):
    def get(self , request , ClassName , SubjectName):
        if Pr_Classes.objects.filter(classes=ClassName).exists():
                if Pr_Subject.objects.filter(subject=SubjectName).exists():
                        Subject = Pr_Subject.objects.get(subject=SubjectName)
                        SubjectId = Subject.id
                        Class = Pr_Classes.objects.get(classes=ClassName)
                        ClassId = Class.id
                        json_res          = []
                        sql               = "select DISTINCT Beezaccs_pr_uint.id , Beezaccs_pr_uint.Uint from Beezaccs_pr_uint inner join Beezaccs_pr_exercisesonline on Beezaccs_pr_uint.id = Beezaccs_pr_exercisesonline.unit_id where classes_id=" + str(ClassId) + " and subject_id=" + str(SubjectId) + " order by Beezaccs_pr_uint.id"
                        Exersise_ID       = Pr_Uint.objects.raw(sql)
                        for record in Exersise_ID: 
                                json_obj  = dict(ID = record.id ,Uint = record.Uint)
                                json_res.append([json_obj])
                        return Response({'Data':json_res})

# API To Return List Topics Related To Custom class and Custom subjects and Custom Unit
class prTopics(generics.GenericAPIView):
    def get(self , request , UnitName):
        if Pr_Uint.objects.filter(Uint='going to the seaside').exists():
                unit = Pr_Uint.objects.get(Uint='going to the seaside')
                unitId = unit.id
                import re
                name = 'Camelcasename'
                name = re.sub(r'(?<!^)(?=[A-Z])', ' ', name).lower()
                # name = re.sub(r'(?<!^)(?=[A-Z])', '_', UnitName).lower()
                print(name)  # camel_case_name
                name = ''.join(word.title() for word in UnitName.split('_'))
                print(name)
                json_res          = []
                sql               = "select DISTINCT Beezaccs_pr_topic.id , Beezaccs_pr_topic.Topic from Beezaccs_pr_topic inner join Beezaccs_pr_exercisesonline on Beezaccs_pr_topic.id = Beezaccs_pr_exercisesonline.topic_id where unit_id=" + str(unitId)
                Exersise_ID       = Pr_Topic.objects.raw(sql)
                for record in Exersise_ID: 
                        json_obj  = dict(ID = record.id ,Topic = record.Topic)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Return List Uints And Topic Related To Custom class and Custom Subject
class prUnitsTopics(generics.GenericAPIView):
    def get(self , request , ClassName , SubjectName):
        if Pr_Classes.objects.filter(classes=ClassName).exists():
                if Pr_Subject.objects.filter(subject=SubjectName).exists():
                        sub = Pr_Subject.objects.get(subject=SubjectName)
                        sub_id = sub.id
                        cl = Pr_Classes.objects.get(classes=ClassName)
                        cl_id = cl.id
                        json_res      = []
                        sql           = "SELECT DISTINCT Beezaccs_pr_exercisesonline.topic_id , Beezaccs_pr_topic.Topic , Beezaccs_pr_uint.id , Beezaccs_pr_uint.Uint from Beezaccs_pr_exercisesonline inner join Beezaccs_pr_topic on Beezaccs_pr_topic.id = Beezaccs_pr_exercisesonline.topic_id inner join Beezaccs_pr_uint on Beezaccs_pr_uint.id = Beezaccs_pr_exercisesonline.unit_id WHERE classes_id=" + str(cl_id) + " and subject_id=" + str(sub_id) + " order by Beezaccs_pr_uint.id"
                        Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                        for record in Exersise_ID: 
                                json_obj  = dict(IDUnit = record.id, Unit = record.Uint, IDTopic = record.topic_id, Topic = record.Topic )
                                json_res.append([json_obj])
                        return Response({'Data':json_res})

# API To Return Summary Related To Custom Topic
class prSummary(generics.GenericAPIView):
    def get(self , request , TobicName):
        if Pr_Topic.objects.filter(Topic=TobicName).exists():
                        topic = Pr_Topic.objects.get(Topic=TobicName)
                        TopicId = topic.id
                        json_res          = []
                        sql               = "select id , subject , Text , image01 , image02 , alternative_image01 , alternative_image02 from Beezaccs_pr_summary where topic_id=" + str(TopicId)
                        Summary_ID        = Pr_Summary.objects.raw(sql)
                        URLROOT           = 'https://publicws.bzacd.com'
                        for record in Summary_ID: 
                                json_obj  = dict(ID = record.id , subject = record.subject , Text = record.Text , Image01 = URLROOT+record.image01.url , Image02 = URLROOT+record.image02.url)
                                json_res.append([json_obj])
                        return Response({'Data':json_res})

# API To Return Exercises Related To Custom Topic
class prExercises(generics.GenericAPIView):
    def get(self , request , ClassName , SubjectName , UnitName , TopicName):
        if Pr_Classes.objects.filter(classes=ClassName).exists():
                        if Pr_Subject.objects.filter(subject=SubjectName).exists():
                                if Pr_Uint.objects.filter(Uint=UnitName).exists():
                                        if Pr_Topic.objects.filter(Topic=TopicName).exists():
                                                cl = Pr_Classes.objects.get(classes=ClassName)
                                                cl_id = cl.id
                                                sub = Pr_Subject.objects.get(subject=SubjectName)
                                                sub_id = sub.id
                                                unit = Pr_Uint.objects.get(Uint=UnitName)
                                                unit_id = unit.id
                                                top = Pr_Topic.objects.get(Topic=TopicName)
                                                topic_id = top.id
                                                json_res          = []
                                                sql               = "SELECT be.id , be.level_id , be.classes_id , be.subject_id , be.unit_id , be.topic_id , be.exercisetypy_id , be.exercise , be.is_Done , be.is_Free , be.is_True_id , be.A , be.B , be.C , be.D , be.A_Image , be.B_Image , be.C_Image , be.D_Image , be.alternative_A_Image , be.alternative_B_Image , be.alternative_C_Image , be.alternative_D_Image , be.created_at , be.updated_at , be.File , be.image , be.alternative_image , bt.istrue FROM Beezaccs_pr_exercisesonline be inner join Beezaccs_pr_is_true bt on be.is_True_id=bt.id WHERE unit_id=" + str(unit_id) + " AND topic_id=" + str(topic_id) + " AND subject_id=" + str(sub_id) + " and classes_id =" + str(cl_id) + " ORDER BY be.id"
                                                Exersise_ID       = Pr_ExercisesOnline.objects.raw(sql)
                                                Exersise_Total    = Pr_ExercisesOnline.objects.filter(unit_id=unit_id , topic_id=topic_id , subject_id=sub_id , classes_id=cl_id).count()
                                                URLROOT           = 'https://publicws.bzacd.com'
                                                for record in Exersise_ID: 
                                                        json_obj  = dict(IDExercises = record.id , Exercise = record.exercise , IsDone = record.is_Done , IsFree = record.is_Free , A = record.A , B = record.B , C = record.C , D = record.D , A_Image = URLROOT+record.A_Image.url , B_Image = URLROOT+record.B_Image.url , C_Image = URLROOT+record.C_Image.url , D_Image = URLROOT+record.D_Image.url , alternative_A_Image = record.alternative_A_Image , alternative_B_Image = record.alternative_B_Image , alternative_C_Image = record.alternative_C_Image , alternative_D_Image = record.alternative_D_Image  , created_at =  record.created_at , updated_at = record.updated_at , File = URLROOT+record.File.url , Image = URLROOT+record.image.url ,alternative_image = record.alternative_image, Subject = record.subject_id , Classes = record.classes_id , ExerciseType = record.exercisetypy_id  , Level = record.level_id , Unit = record.unit_id , Topic = record.topic_id)
                                                        json_res.append([json_obj])
                                                return Response({'Count':Exersise_Total , 'Data':json_res})

# API To Return Custom Exercise
class prExercise(generics.GenericAPIView):
        def get(self , request , ID):
                json_res      = []
                sql           = "Select * from Beezaccs_pr_exercisesonline where id="+ID
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                URLROOT       = 'https://publicws.bzacd.com'
                for record in Exersise_ID:
                        json_obj  = dict(IDExercises = record.id , Exercise = record.exercise , IsDone = record.is_Done , IsFree = record.is_Free , A = record.A , B = record.B , C = record.C , D = record.D , A_Image = URLROOT+record.A_Image.url , B_Image = URLROOT+record.B_Image.url  , C_Image = URLROOT+record.C_Image.url , D_Image = URLROOT+record.D_Image.url , alternative_A_Image = record.alternative_A_Image , alternative_B_Image = record.alternative_B_Image , alternative_C_Image = record.alternative_C_Image , alternative_D_Image = record.alternative_D_Image , created_at =  record.created_at , updated_at = record.updated_at , File = URLROOT+record.File.url , Image = URLROOT+record.image.url,alternative_image = record.alternative_image, Subject = record.subject_id , Classes = record.classes_id , ExerciseType = record.exercisetypy_id  , Level = record.level_id , Unit = record.unit_id , Topic = record.topic_id)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Return List True Answer Related To Custom class and Custom categories and Custom Topic and Custom SubTopic
class prAnswerExercises(generics.GenericAPIView):
        def get(self , request , ClassName , SubjectName , UnitName , TopicName):
                if Pr_Classes.objects.filter(classes=ClassName).exists():
                        if Pr_Subject.objects.filter(subject=SubjectName).exists():
                                if Pr_Uint.objects.filter(Uint=UnitName).exists():
                                        if Pr_Topic.objects.filter(Topic=TopicName).exists():
                                                cl = Pr_Classes.objects.get(classes=ClassName)
                                                cl_id = cl.id
                                                sub = Pr_Subject.objects.get(subject=SubjectName)
                                                sub_id = sub.id
                                                unit = Pr_Uint.objects.get(Uint=UnitName)
                                                unit_id = unit.id
                                                top = Pr_Topic.objects.get(Topic=TopicName)
                                                topic_id = top.id
                                                json_res      = []
                                                sql           = "select Beezaccs_pr_exercisesonline.id , Beezaccs_pr_is_true.istrue  from Beezaccs_pr_exercisesonline inner join Beezaccs_pr_is_true on Beezaccs_pr_exercisesonline.is_True_id=Beezaccs_pr_is_true.id where unit_id=" + str(unit_id) + " and topic_id =" + str(topic_id) + " and subject_id=" + str(sub_id) + " and classes_id =" + str(cl_id) + " order by Beezaccs_pr_exercisesonline.id"
                                                sqlTotal      = Pr_ExercisesOnline.objects.filter(unit_id=unit_id , topic_id=topic_id , subject_id=sub_id , classes_id=cl_id).count()
                                                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                                                for record in Exersise_ID:
                                                        json_obj  = dict(IDExercises = record.id , TrueAnswer = record.istrue)
                                                        json_res.append([json_obj])
                                                return Response({'Count':sqlTotal , 'Data':json_res})

# API To Return True Answer Related To Custom Exercise
class prAnswerExercise(generics.GenericAPIView):
        def get(self , request , ID):
                json_res      = []
                sql           = "select Beezaccs_pr_exercisesonline.id , Beezaccs_pr_is_true.istrue from Beezaccs_pr_exercisesonline inner join Beezaccs_pr_is_true on Beezaccs_pr_exercisesonline.is_True_id=Beezaccs_pr_is_true.id where Beezaccs_pr_exercisesonline.id="+ID
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        json_obj  = dict(TrueAnswer = record.istrue)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Return Result About Answer User
class prResultAnswer(generics.GenericAPIView):
        def get(self , request , ID , Answer):
                json_res      = []
                sql           = "select Beezaccs_pr_exercisesonline.id , Beezaccs_pr_is_true.istrue from Beezaccs_pr_exercisesonline inner join Beezaccs_pr_is_true on Beezaccs_pr_exercisesonline.is_True_id=Beezaccs_pr_is_true.id where Beezaccs_pr_exercisesonline.id="+ID
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.istrue==Answer):
                                return Response({'Data':'True'})
                        else:
                                return Response({'Data':'False'})

# API To Link Exercise To User
class prInsertExercise(generics.GenericAPIView):
        def get(self , request , ID_user , ID_exercise , Time , Answer , TrueAnswer):
                user = User.objects.filter(id=ID_user)
                for record in user:
                        IdUser  = record.id
                Pr_Link_Exercises.objects.create(user=IdUser,exercise=ID_exercise,duration_Time=Time,answer=Answer,true_answer=TrueAnswer)
                return Response({'Data':'Successfully Added'})

# API To All Lavel

# API Teasher
# API To Return All Data To User
class UserDetails(generics.GenericAPIView):
        def get(self , request , ID_user):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT au.id , au.first_name , au.last_name , au.Dob , au.Avatar , au.live , bs.name , kg.classes FROM Beezaccs_studentschoole as ss inner join Beezaccs_schoole as bs on ss.schoole_id=bs.id inner join accounts_user as au on au.id=ss.student_id inner join Beezaccs_studentclass as bsc on bsc.student_id=ss.student_id inner join Beezaccs_classes as kg on kg.id=bsc.kgclass_id where au.id="+ID_user
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com/'
                                for record in Exersise_ID:
                                        json_obj  = dict(FirstName = record.first_name , LastName = record.last_name , Dob = record.Dob  ,  Avatar = URLROOT+record.Avatar, live = record.live , SchooleName = record.name , className = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT au.id , au.first_name , au.last_name , au.Dob , au.Avatar , au.live , bs.name , pr.classes FROM Beezaccs_studentschoole as ss inner join Beezaccs_schoole as bs on ss.schoole_id=bs.id inner join accounts_user as au on au.id=ss.student_id inner join Beezaccs_studentclass as bsc on bsc.student_id=ss.student_id inner join Beezaccs_pr_classes as pr on pr.id=bsc.prclass_id where au.id="+ID_user
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com/'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(FirstName = record.first_name , LastName = record.last_name , Dob = record.Dob  ,  Avatar = URLROOT+record.Avatar, live = record.live , SchooleName = record.name , className = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT au.id , au.first_name , au.last_name , au.Dob , au.Avatar , au.live , bs.name , mid.classes FROM Beezaccs_studentschoole as ss inner join Beezaccs_schoole as bs on ss.schoole_id=bs.id inner join accounts_user as au on au.id=ss.student_id inner join Beezaccs_studentclass as bsc on bsc.student_id=ss.student_id inner join Beezaccs_mid_classes as mid on mid.id=bsc.midclass_id where au.id="+ID_user
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com/'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(FirstName = record.first_name , LastName = record.last_name , Dob = record.Dob  ,  Avatar = URLROOT+record.Avatar, live = record.live , SchooleName = record.name , className = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return active tasks Details
class ActiveTasks(generics.GenericAPIView):
        def get(self , request , ID_user):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "select bs.id , count(bs.AssignmentType_id) as Total , bp.Procedure , bkc.category , Beezaccs_section.title , Beezaccs_classes.classes from Beezaccs_studentassignment as bs INNER join Beezaccs_kin_categoriesclass as bkc on bkc.id=bs.kgsubject_id INNER join Beezaccs_procedure as bp on bp.id=bs.AssignmentType_id INNER join Beezaccs_section on Beezaccs_section.id=bs.Section_id INNER join Beezaccs_classes on Beezaccs_classes.id=bs.kgclass_id where bs.level_id=1 and student_id="+ID_user+" GROUP BY kgsubject_id , AssignmentType_id , Section_id , kgclass_id ORDER by Beezaccs_classes.classes , Beezaccs_section.title , bkc.category"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(Total = record.Total , Procedure = record.Procedure   ,  Subject = record.category, SectionName = record.title , Classes = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "select bs.id , count(bs.AssignmentType_id) as Total , bp.Procedure , bkc.subject , Beezaccs_section.title , Beezaccs_pr_classes.classes from Beezaccs_studentassignment as bs INNER join Beezaccs_pr_subject as bkc on bkc.id=bs.prsubject_id INNER join Beezaccs_procedure as bp on bp.id=bs.AssignmentType_id INNER join Beezaccs_section on Beezaccs_section.id=bs.Section_id INNER join Beezaccs_pr_classes on Beezaccs_pr_classes.id=bs.prclass_id where bs.level_id=2 and student_id="+ID_user+" GROUP BY kgsubject_id , AssignmentType_id , Section_id , kgclass_id ORDER by Beezaccs_classes.classes , Beezaccs_section.title , bkc.subject"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(Total = record.Total , Procedure = record.Procedure   ,  Subject = record.subject, SectionName = record.title , Classes = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "select bs.id , count(bs.AssignmentType_id) as Total , bp.Procedure , bkc.subject , Beezaccs_section.title , Beezaccs_mid_classes.classes from Beezaccs_studentassignment as bs INNER join Beezaccs_mid_subject as bkc on bkc.id=bs.midsubject_id INNER join Beezaccs_procedure as bp on bp.id=bs.AssignmentType_id INNER join Beezaccs_section on Beezaccs_section.id=bs.Section_id INNER join Beezaccs_mid_classes on Beezaccs_mid_classes.id=bs.midclass_id where bs.level_id=3 and student_id="+ID_user+" GROUP BY kgsubject_id , AssignmentType_id , Section_id , kgclass_id ORDER by Beezaccs_classes.classes , Beezaccs_section.title , bkc.subject"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total , Procedure = record.Procedure   ,  Subject = record.subject, SectionName = record.title , Classes = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return All Data To User
class Posts(generics.GenericAPIView):
        def get(self , request , ID_user , Par):
                if (Par=='0'):
                        json_like     = []
                        json_comment  = []
                        json_post     = []
                        sql           = "SELECT COUNT(bl.id) AS TotalLike , bp.id , bp.title , bp.post , bp.image , bp.created_at , au.first_name , au.last_name , au.Avatar FROM Beezaccs_post AS bp LEFT OUTER JOIN Beezaccs_like AS bl on bp.id=bl.post_id inner join accounts_user AS au on bp.user_id=au.id where bp.user_id="+ID_user+" GROUP BY bp.id , bp.title , bp.post , bp.image , bp.created_at , au.first_name , au.last_name , au.Avatar LIMIT 5"
                        sql1          = "SELECT COUNT(bc.id) as TotalComment , bp.id , bp.title , bp.post , bp.image , bp.created_at , au.first_name , au.last_name , au.Avatar FROM Beezaccs_post AS bp LEFT OUTER JOIN Beezaccs_comment AS bc on bp.id=bc.post_id inner join accounts_user AS au on bp.user_id=au.id where bp.user_id="+ID_user+" GROUP BY bp.id , bp.title , bp.post , bp.image , bp.created_at , au.first_name , au.last_name , au.Avatar LIMIT 5"
                        Exersise_ID   = Post.objects.raw(sql)
                        Exersise_ID1  = Post.objects.raw(sql1)
                        URLROOT       = 'https://publicws.bzacd.com'
                        for record in Exersise_ID:
                                json_obj  = dict(TotalLike = record.TotalLike , Post_Id = record.id)
                                json_like.append([json_obj])
                        for record in Exersise_ID1:
                                json_obj = dict(TotalComment = record.TotalComment, Post_Id = record.id)
                                json_comment.append([json_obj])
                        for record in Exersise_ID:
                                json_obj = dict(Post_Id = record.id , Image = URLROOT+record.image.url , Created_at = record.created_at , FirstName_Author = record.first_name , LastName_Author = record.last_name ,  Avatar_Author = URLROOT+record.Avatar , Title = record.title , Post = record.post)
                                json_post.append([json_obj])
                        return Response({'Like':json_like,'Comment':json_comment,'Post':json_post})
                else:
                        json_like     = []
                        json_comment  = []
                        json_post     = []
                        sql           = "SELECT COUNT(bl.id) AS TotalLike , bp.id , bp.title , bp.post , bp.image , bp.created_at , au.first_name , au.last_name , au.Avatar FROM Beezaccs_post AS bp LEFT OUTER JOIN Beezaccs_like AS bl on bp.id=bl.post_id inner join accounts_user AS au on bp.user_id=au.id where bp.user_id="+ID_user+" GROUP BY bp.id , bp.title , bp.post , bp.image , bp.created_at , au.first_name , au.last_name , au.Avatar LIMIT "+Par+" , 5"
                        sql1          = "SELECT COUNT(bc.id) as TotalComment , bp.id , bp.title , bp.post , bp.image , bp.created_at , au.first_name , au.last_name , au.Avatar FROM Beezaccs_post AS bp LEFT OUTER JOIN Beezaccs_comment AS bc on bp.id=bc.post_id inner join accounts_user AS au on bp.user_id=au.id where bp.user_id="+ID_user+" GROUP BY bp.id , bp.title , bp.post , bp.image , bp.created_at , au.first_name , au.last_name , au.Avatar LIMIT "+Par+" , 5"
                        Exersise_ID   = Post.objects.raw(sql)
                        Exersise_ID1  = Post.objects.raw(sql1)
                        URLROOT       = 'https://publicws.bzacd.com'
                        for record in Exersise_ID:
                                json_obj  = dict(TotalLike = record.TotalLike , Post_Id = record.id)
                                json_like.append([json_obj])
                        for record in Exersise_ID1:
                                json_obj = dict(TotalComment = record.TotalComment, Post_Id = record.id)
                                json_comment.append([json_obj])
                        for record in Exersise_ID:
                                json_obj = dict(Post_Id = record.id , Image = URLROOT+record.image.url , Created_at = record.created_at , FirstName_Author = record.first_name , LastName_Author = record.last_name ,  Avatar_Author = URLROOT+record.Avatar , Title = record.title , Post = record.post)
                                json_post.append([json_obj])
                        return Response({'Like':json_like,'Comment':json_comment,'Post':json_post})

# API To Return Like To Post
class LikePost(generics.GenericAPIView):
        def get(self , request , ID_post):
                json_res      = []
                sql           = Like.objects.filter(post_id=ID_post).count()
                sql1          = "SELECT bl.id , bl.Like , au.first_name , au.last_name , au.Avatar FROM Beezaccs_like as bl INNER JOIN accounts_user as au on bl.user_id=au.id where post_id="+ID_post
                URLROOT       = 'https://publicws.bzacd.com'
                Exersise_ID  = Post.objects.raw(sql1)
                for record in Exersise_ID:
                        json_obj = dict(Like  = record.Like , First_Name  = record.first_name , Last_Name  = record.last_name , Avatar = URLROOT+record.Avatar)
                        json_res.append([json_obj])
                return Response({'Count':sql ,'Data':json_res})

# API To Return Comment To Post
class CommentPost(generics.GenericAPIView):
        def get(self , request , ID_post):
                json_res      = []
                sql           = Comment.objects.filter(post_id=ID_post).count()
                sql1          = "SELECT bc.id , bc.Comment , au.first_name , au.last_name , au.Avatar , bc.created_at FROM Beezaccs_comment as bc INNER JOIN accounts_user as au on bc.user_id=au.id where post_id="+ID_post
                URLROOT       = 'https://publicws.bzacd.com'
                Exersise_ID1  = Post.objects.raw(sql1)
                for record1 in Exersise_ID1:
                        json_obj1 = dict(Comment  = record1.Comment , First_Name  = record1.first_name , Last_Name  = record1.last_name , Avatar = URLROOT+record1.Avatar , Created_at = record1.created_at)
                        json_res.append([json_obj1])
                return Response({'Count':sql ,'Data':json_res})

# API To Return Class Subject Left Nav Bar
class ThClassSubject(generics.GenericAPIView):
        def get(self , request , ID_user):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "select distinct bkc.category , bkc.id, Beezaccs_section.title , Beezaccs_classes.classes , bs.kgsubject_id , bs.kgclass_id , bs.Section_id from Beezaccs_studentassignment as bs INNER join Beezaccs_kin_categoriesclass as bkc on bkc.id=bs.kgsubject_id INNER join Beezaccs_procedure as bp on bp.id=bs.AssignmentType_id INNER join Beezaccs_section on Beezaccs_section.id=bs.Section_id INNER join Beezaccs_classes on Beezaccs_classes.id=bs.kgclass_id where bs.level_id=1 and student_id=26 GROUP BY kgsubject_id , AssignmentType_id , Section_id , kgclass_id ORDER by Beezaccs_classes.classes , Beezaccs_section.title , bkc.category"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ClassID = record.kgclass_id , ClassName = record.classes , SectionID = record.Section_id , SectionName = record.title , SubjectID = record.kgsubject_id ,  SubjectName = record.category)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "select distinct bkc.subject , bkc.id, Beezaccs_section.title , Beezaccs_pr_classes.classes , bs.prsubject_id , bs.prclass_id , bs.Section_id  from Beezaccs_studentassignment as bs INNER join Beezaccs_pr_subject as bkc on bkc.id=bs.prsubject_id INNER join Beezaccs_procedure as bp on bp.id=bs.AssignmentType_id INNER join Beezaccs_section on Beezaccs_section.id=bs.Section_id INNER join Beezaccs_pr_classes on Beezaccs_pr_classes.id=bs.prclass_id where bs.level_id=2 and student_id="+ID_user+" GROUP BY prsubject_id , AssignmentType_id , Section_id , prclass_id ORDER by Beezaccs_pr_classes.classes , Beezaccs_section.title , bkc.subject"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ClassID = record.prclass_id , ClassName = record.classes , SectionID = record.Section_id , SectionName = record.title , SubjectID = record.prsubject_id , SubjectName = record.subject)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "select distinct bkc.subject , bkc.id, Beezaccs_section.title , Beezaccs_mid_classes.classes , bs.midsubject_id , bs.midclass_id , bs.Section_id  from Beezaccs_studentassignment as bs INNER join Beezaccs_mid_subject as bkc on bkc.id=bs.midsubject_id INNER join Beezaccs_procedure as bp on bp.id=bs.AssignmentType_id INNER join Beezaccs_section on Beezaccs_section.id=bs.Section_id INNER join Beezaccs_mid_classes on Beezaccs_mid_classes.id=bs.midclass_id where bs.level_id=3 and student_id="+ID_user+" GROUP BY midsubject_id , AssignmentType_id , Section_id , midclass_id ORDER by Beezaccs_mid_classes.classes , Beezaccs_section.title , bkc.subject"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ClassID = record.midclass_id , ClassName = record.classes , SectionID = record.Section_id , SectionName = record.title , SubjectID = record.midsubject_id , SubjectName = record.subject)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return Procedure Left Nav Bar
class ThProcedure(generics.GenericAPIView):
        def get(self , request):
                json_res      = []
                sql           = "SELECT bp.id , bp.Procedure FROM Beezaccs_procedure as bp ORDER BY id"
                URLROOT       = 'https://publicws.bzacd.com'
                Exersise_ID   = Post.objects.raw(sql)
                for record in Exersise_ID:
                        json_obj  = dict(ProcedureID = record.id , ProcedureName = record.Procedure)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Return Class
class ThClass(generics.GenericAPIView):
        def get(self , request , ID_user):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT bc.id , bc.classes FROM  Beezaccs_classes as bc ORDER BY bc.id"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.id , Class = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT bc.id , bc.classes FROM  Beezaccs_pr_classes as bc ORDER BY bc.id"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.id , Class = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT bc.id , bc.classes FROM  Beezaccs_mid_classes as bc ORDER BY bc.id"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.id , Class = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return Subject
class ThSubject(generics.GenericAPIView):
        def get(self , request , ID_user , ID_class):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT bkc.id , bkc.category FROM Beezaccs_kin_categoriesclass as bkc"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.id , Subject = record.category)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT bkc.id , bkc.subject FROM Beezaccs_pr_subject as bkc"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.id , Subject = record.subject)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT bkc.id , bkc.subject FROM Beezaccs_mid_subject as bkc"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.id , Subject = record.subject)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return Unit
class ThUnit(generics.GenericAPIView):
        def get(self , request , ID_user , ID_class , ID_subject):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT DISTINCT bke.topic_id , bt.id , bt.Topic FROM Beezaccs_kin_exercisesonline as bke INNER JOIN Beezaccs_topic as bt on bke.topic_id=bt.id WHERE bke.categories_id="+ID_subject+" and bke.classes_id="+ID_class
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.topic_id , Unit = record.Topic)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT DISTINCT bke.unit_id , bt.id , bt.Uint FROM Beezaccs_pr_exercisesonline as bke INNER JOIN Beezaccs_pr_uint as bt on bke.unit_id=bt.id WHERE bke.subject_id="+ID_subject+" and bke.classes_id="+ID_class
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.unit_id , Unit = record.Uint)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT DISTINCT bke.unit_id , bt.id , bt.Uint FROM Beezaccs_mid_exercisesonline as bke INNER JOIN Beezaccs_mid_uint as bt on bke.unit_id=bt.id WHERE bke.subject_id="+ID_subject+" and bke.classes_id="+ID_class 
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.unit_id , Unit = record.Uint)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return Unit
class ThTopic(generics.GenericAPIView):
        def get(self , request , ID_user , ID_class , ID_subject , ID_unit):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT DISTINCT bke.sub_topic_id , bt.id , bt.Sub_Topic FROM Beezaccs_kin_exercisesonline as bke INNER JOIN Beezaccs_sub_topic as bt on bke.sub_topic_id=bt.id WHERE bke.categories_id="+ID_subject+" AND bke.topic_id="+ID_unit+" and bke.classes_id="+ID_class
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.sub_topic_id , Topic = record.Sub_Topic)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT DISTINCT bke.topic_id , bt.id , bt.Topic FROM Beezaccs_pr_exercisesonline as bke INNER JOIN Beezaccs_pr_topic as bt on bke.topic_id=bt.id WHERE bke.subject_id="+ID_subject+" AND bke.unit_id="+ID_unit+" and bke.classes_id="+ID_class
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.topic_id , Topic = record.Topic)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT DISTINCT bke.topic_id , bt.id , bt.Topic FROM Beezaccs_mid_exercisesonline as bke INNER JOIN Beezaccs_mid_topic as bt on bke.topic_id=bt.id WHERE bke.subject_id="+ID_subject+"  AND bke.unit_id="+ID_unit+" and bke.classes_id="+ID_class
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.unit_id , Unit = record.Uint)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return Question Type
class ThQuestionType(generics.GenericAPIView):
        def get(self , request , ID_user):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT bpe.id , bpe.exercisetypy FROM Beezaccs_exersisetype as bpe order by bpe.id"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.id , Type = record.exercisetypy)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT bpe.id , bpe.exercisetypy FROM Beezaccs_pr_exersisetype as bpe order by bpe.id"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.id , Type = record.exercisetypy)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT bpe.id , bpe.exercisetypy FROM Beezaccs_mid_exersisetype as bpe order by bpe.id"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.id , Type = record.exercisetypy)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return Correct Answer
class ThCorrectAnswer(generics.GenericAPIView):
        def get(self , request , ID_user):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT bit.id , bit.istrue  FROM Beezaccs_is_true as bit where id=1 or id=2 or id=3 or id=4"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.id , istrue = record.istrue)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT bit.id , bit.istrue  FROM Beezaccs_pr_is_true as bit where id=1 or id=2 or id=3 or id=4"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.id , istrue = record.istrue)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT bit.id , bit.istrue  FROM Beezaccs_mid_is_true as bit where id=1 or id=2 or id=3 or id=4"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ID = record.id , istrue = record.istrue)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Insert Question To User
class ThInsertQuestion(generics.GenericAPIView):
        def post(self , request , ID_user , ID_class , ID_subject , ID_unit , ID_topic , ID_type , question , A , B , C , D , ID_correct , Explanation):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                level         = Level.objects.get(id=record.level_id)
                                classes       = Classes.objects.get(id=ID_class)
                                categories    = Kin_CategoriesClass.objects.get(id=ID_subject)
                                topic         = Topic.objects.get(id=ID_unit)
                                sub_topic     = Sub_Topic.objects.get(id=ID_topic)
                                exercisetypy  = ExersiseType.objects.get(id=ID_type)
                                is_true       = is_True.objects.get(id=ID_correct)
                                Kin_ExercisesOnline.objects.create(level=level,classes=classes,categories=categories,topic=topic,sub_topic=sub_topic,exercisetypy=exercisetypy,exercise=question,A=A,B=B,C=C,D=D,is_True=is_true,explanation=Explanation)
                                return Response({'Data':'Successfully Added'})
                        if (record.level_id==2):
                                level         = Level.objects.get(id=record.level_id)
                                classes       = Pr_Classes.objects.get(id=ID_class)
                                categories    = Pr_Subject.objects.get(id=ID_subject)
                                topic         = Pr_Uint.objects.get(id=ID_unit)
                                sub_topic     = Pr_Topic.objects.get(id=ID_topic)
                                exercisetypy  = Pr_ExersiseType.objects.get(id=ID_type)
                                is_true       = Pr_is_True.objects.get(id=ID_correct)
                                Pr_ExercisesOnline.objects.create(level=record.level_id,classes=classes,subject=categories,unit=topic,topic=sub_topic,exercisetypy=exercisetypy,exercise=question,A=A,B=B,C=C,D=D,is_True=is_true,explanation=Explanation)
                                return Response({'Data':'Successfully Added'})
                        else:
                                level         = Level.objects.get(id=record.level_id)
                                classes       = Mid_Classes.objects.get(id=ID_class)
                                categories    = Mid_Subject.objects.get(id=ID_subject)
                                topic         = Mid_Uint.objects.get(id=ID_unit)
                                sub_topic     = Mid_Topic.objects.get(id=ID_topic)
                                exercisetypy  = Mid_ExersiseType.objects.get(id=ID_type)
                                is_true       = Mid_is_True.objects.get(id=ID_correct)
                                Mid_ExercisesOnline.objects.create(level=record.level_id,classes=classes,subject=categories,unit=topic,topic=sub_topic,exercisetypy=exercisetypy,exercise=question,A=A,B=B,C=C,D=D,is_True=is_true,explanation=Explanation)
                                return Response({'Data':'Successfully Added'})

# API To Return Type Topic
class ThTypeTopic(generics.GenericAPIView):
        def get(self , request):
                json_res      = []
                sql           = "SELECT tt.id , tt.TopicType FROM Beezaccs_topictype as tt ORDER BY id"
                URLROOT       = 'https://publicws.bzacd.com'
                Exersise_ID   = Post.objects.raw(sql)
                for record in Exersise_ID:
                        json_obj  = dict(TopicTypeID = record.id , TopicType = record.TopicType)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Return Duration Time
class ThDurationTime(generics.GenericAPIView):
        def get(self , request):
                json_res      = []
                sql           = "SELECT tt.id , tt.Duration FROM Beezaccs_durationtime as tt ORDER BY id"
                URLROOT       = 'https://publicws.bzacd.com'
                Exersise_ID   = Post.objects.raw(sql)
                for record in Exersise_ID:
                        json_obj  = dict(DurationID = record.id , Duration = record.Duration)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Insert Assignment To Section
class ThInsertAssignment(generics.GenericAPIView):
        def post(self , request , ID_user , ID_pro_Type , ID_class , ID_section , ID_subject , ID_unit , ID_topic , ID_type , submissiondate , ID_duration):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                student       = User.objects.get(id=ID_user)
                                level         = Level.objects.get(id=record.level_id)
                                procedure     = Procedure.objects.get(id=ID_pro_Type)
                                classes       = Classes.objects.get(id=ID_class)
                                categories    = Kin_CategoriesClass.objects.get(id=ID_subject)
                                topic         = Topic.objects.get(id=ID_unit)
                                sub_topic     = Sub_Topic.objects.get(id=ID_topic)
                                topictypy     = TopicType.objects.get(id=ID_type)
                                duration      = DurationTime.objects.get(id=ID_duration)
                                section       = Section.objects.get(id=ID_section)
                                StudentAssignment.objects.create(student=student,level=level,kgclass=classes,kgsubject=categories,kguint=topic,kgtopic=sub_topic,AssignmentType=procedure,TopicType=topictypy,Section=section,DurationTime=duration,submissionDate=submissiondate)
                                return Response({'Data':'Successfully Added'})
                        if (record.level_id==2):
                                student       = User.objects.get(id=ID_user)
                                level         = Level.objects.get(id=record.level_id)
                                procedure     = Procedure.objects.get(id=ID_pro_Type)
                                classes       = Pr_Classes.objects.get(id=ID_class)
                                categories    = Pr_Subject.objects.get(id=ID_subject)
                                topic         = Pr_Uint.objects.get(id=ID_unit)
                                sub_topic     = Pr_Topic.objects.get(id=ID_topic)
                                topictypy     = Pr_ExersiseType.objects.get(id=ID_type)
                                duration      = Pr_is_True.objects.get(id=ID_duration)
                                section       = Section.objects.get(id=ID_section)
                                StudentAssignment.objects.create(student=student,level=level,prclass=classes,prsubject=categories,pruint=topic,prtopic=sub_topic,AssignmentType=procedure,TopicType=topictypy,Section=section,DurationTime=duration,submissionDate=submissiondate)
                                return Response({'Data':'Successfully Added'})
                        else:
                                student       = User.objects.get(id=ID_user)
                                level         = Level.objects.get(id=record.level_id)
                                procedure     = Procedure.objects.get(id=ID_pro_Type)
                                classes       = Mid_Classes.objects.get(id=ID_class)
                                categories    = Mid_Subject.objects.get(id=ID_subject)
                                topic         = Mid_Uint.objects.get(id=ID_unit)
                                sub_topic     = Mid_Topic.objects.get(id=ID_topic)
                                topictypy     = Mid_ExersiseType.objects.get(id=ID_type)
                                duration      = Mid_is_True.objects.get(id=ID_duration)
                                section       = Section.objects.get(id=ID_section)
                                StudentAssignment.objects.create(student=student,level=level,midclass=classes,midsubject=categories,mduint=topic,mdtopic=sub_topic,AssignmentType=procedure,TopicType=topictypy,Section=section,DurationTime=duration,submissionDate=submissiondate)
                                return Response({'Data':'Successfully Added'})

# API To Return All Section
class ThSection(generics.GenericAPIView):
        def get(self , request):
                json_res      = []
                sql           = "SELECT tt.id , tt.section FROM Beezaccs_section as tt ORDER BY id"
                URLROOT       = 'https://publicws.bzacd.com'
                Exersise_ID   = Post.objects.raw(sql)
                for record in Exersise_ID:
                        json_obj  = dict(SectionID = record.id , Section = record.section)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Insert Section
class ThInsertSection(generics.GenericAPIView):
        def post(self , request , SectionName):
                if Section.objects.filter(section=SectionName).exists():
                        section = Section.objects.get(section=SectionName)
                        sectionId = section.id
                        json_res      = []
                        sql           = "SELECT bs.id , bs.section FROM Beezaccs_section bs where id=" + str(sectionId)
                        IDClass       = Section.objects.raw(sql)
                        for record in IDClass:
                                json_obj  = dict(ID = record.id , Section=record.section)
                                json_res.append([json_obj])
                        return Response({'Data':'The Section Exists','Data Is':json_res})
                else:
                        Section.objects.create(title=SectionName,section=SectionName)
                        section = Section.objects.get(section=SectionName)
                        sectionId = section.id
                        json_res      = []
                        sql           = "SELECT bs.id , bs.section FROM Beezaccs_section bs where id=" + str(sectionId)
                        IDClass       = Section.objects.raw(sql)
                        for record in IDClass:
                                json_obj  = dict(ID = record.id , Section=record.section)
                                json_res.append([json_obj])
                        return Response({'Data':'The Section Create','Data Is':json_res})

# API Student
# API To Return Class Subject
class StClassSubject(generics.GenericAPIView):
        def get(self , request , ID_user):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "select DISTINCT bkc.category , bkc.id , Beezaccs_classes.id as subjectid , Beezaccs_classes.classes from Beezaccs_studentassignment as bs INNER join Beezaccs_kin_categoriesclass as bkc on bkc.id=bs.kgsubject_id INNER join Beezaccs_classes on Beezaccs_classes.id=bs.kgclass_id where bs.level_id=1 and student_id="+ID_user+" ORDER by bkc.category"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(SubjectID = record.subjectid , Subject = record.category , ClassID = record.id , Class = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "select DISTINCT bkc.subject , bkc.id , Beezaccs_pr_classes.id as subjectid , Beezaccs_pr_classes.classes from Beezaccs_studentassignment as bs INNER join Beezaccs_pr_subject as bkc on bkc.id=bs.prsubject_id INNER join Beezaccs_pr_classes on Beezaccs_pr_classes.id=bs.prclass_id where bs.level_id=2 and student_id="+ID_user+" ORDER by bkc.subject"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(SubjectID = record.subjectid , Subject = record.category , ClassID = record.id , Class = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "select DISTINCT bkc.subject , bkc.id , Beezaccs_mid_classes.id  , Beezaccs_mid_classes.classes from Beezaccs_studentassignment as bs INNER join Beezaccs_mid_subject as bkc on bkc.id=bs.midsubject_id INNER join Beezaccs_mid_classes on Beezaccs_mid_classes.id=bs.prclass_id where bs.level_id=3 and student_id="+ID_user+" ORDER by bkc.subject"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(SubjectID = record.subjectid , Subject = record.category , ClassID = record.id , Class = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return Answer Questions To User
class AnswerQuestions(generics.GenericAPIView):
        def get(self , request , ID_user):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "select ple.id , count(*) as Total from Beezaccs_kin_linkexercises as ple where ple.user="+ID_user
                                sql1          = "select ple.id , count(*) as Easy from Beezaccs_kin_linkexercises as ple inner join Beezaccs_kin_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=1"
                                sql2          = "select ple.id , count(*) as Medium from Beezaccs_kin_linkexercises as ple inner join Beezaccs_kin_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=2"
                                sql3          = "select ple.id , count(*) as Hard from Beezaccs_kin_linkexercises as ple inner join Beezaccs_kin_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=3"
                                URLROOT       = 'https://publicws.bzacd.com'
                                Exersise_ID   = Post.objects.raw(sql)
                                Exersise_ID1  = Post.objects.raw(sql1)
                                Exersise_ID2  = Post.objects.raw(sql2)
                                Exersise_ID3  = Post.objects.raw(sql3)
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total)
                                        json_res.append([json_obj])
                                        for record1 in Exersise_ID1:
                                                json_obj1 = dict(Easy  = record1.Easy)
                                                json_res.append([json_obj1])
                                                for record2 in Exersise_ID2:
                                                        json_obj2 = dict(Medium  = record2.Medium)
                                                        json_res.append([json_obj2])
                                                        for record3 in Exersise_ID3:
                                                                json_obj3 = dict(Hard  = record3.Hard)
                                                                json_res.append([json_obj3])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "select ple.id , count(*) as Total from Beezaccs_pr_link_exercises as ple where ple.user="+ID_user
                                sql1          = "select ple.id , count(*) as Easy from Beezaccs_pr_link_exercises as ple inner join Beezaccs_pr_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_pr_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=1"
                                sql2          = "select ple.id , count(*) as Medium from Beezaccs_pr_link_exercises as ple inner join Beezaccs_pr_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_pr_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=2"
                                sql3          = "select ple.id , count(*) as Hard from Beezaccs_pr_link_exercises as ple inner join Beezaccs_pr_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_pr_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=3"
                                URLROOT       = 'https://publicws.bzacd.com'
                                Exersise_ID   = Post.objects.raw(sql)
                                Exersise_ID1  = Post.objects.raw(sql1)
                                Exersise_ID2  = Post.objects.raw(sql2)
                                Exersise_ID3  = Post.objects.raw(sql3)
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total)
                                        json_res.append([json_obj])
                                        for record1 in Exersise_ID1:
                                                json_obj1 = dict(Easy  = record1.Easy)
                                                json_res.append([json_obj1])
                                                for record2 in Exersise_ID2:
                                                        json_obj2 = dict(Medium  = record2.Medium)
                                                        json_res.append([json_obj2])
                                                        for record3 in Exersise_ID3:
                                                                json_obj3 = dict(Hard  = record3.Hard)
                                                                json_res.append([json_obj3])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "select ple.id , count(*) as Total from Beezaccs_mid_link_exercises as ple where ple.user="+ID_user
                                sql1          = "select ple.id , count(*) as Easy from Beezaccs_mid_link_exercises as ple inner join Beezaccs_mid_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_mid_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=1"
                                sql2          = "select ple.id , count(*) as Medium from Beezaccs_mid_link_exercises as ple inner join Beezaccs_mid_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_mid_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=2"
                                sql3          = "select ple.id , count(*) as Hard from Beezaccs_mid_link_exercises as ple inner join Beezaccs_mid_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_mid_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=3"
                                URLROOT       = 'https://publicws.bzacd.com'
                                Exersise_ID   = Post.objects.raw(sql)
                                Exersise_ID1  = Post.objects.raw(sql1)
                                Exersise_ID2  = Post.objects.raw(sql2)
                                Exersise_ID3  = Post.objects.raw(sql3)
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total)
                                        json_res.append([json_obj])
                                        for record1 in Exersise_ID1:
                                                json_obj1 = dict(Easy  = record1.Easy)
                                                json_res.append([json_obj1])
                                                for record2 in Exersise_ID2:
                                                        json_obj2 = dict(Medium  = record2.Medium)
                                                        json_res.append([json_obj2])
                                                        for record3 in Exersise_ID3:
                                                                json_obj3 = dict(Hard  = record3.Hard)
                                                                json_res.append([json_obj3])
                                return Response({'Data':json_res})

# API To Return Correct Answer Questions To User
class CorrectAnswer(generics.GenericAPIView):
        def get(self , request , ID_user):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "select ple.id , count(*) as Total from Beezaccs_kin_linkexercises as ple where ple.user="+ID_user+" and ple.answer=ple.true_answer"
                                sql1          = "select ple.id , count(*) as Easy from Beezaccs_kin_linkexercises as ple inner join Beezaccs_kin_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=1 and ple.answer=ple.true_answer"
                                sql2          = "select ple.id , count(*) as Medium from Beezaccs_kin_linkexercises as ple inner join Beezaccs_kin_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=2 and ple.answer=ple.true_answer"
                                sql3          = "select ple.id , count(*) as Hard from Beezaccs_kin_linkexercises as ple inner join Beezaccs_kin_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=3 and ple.answer=ple.true_answer"
                                URLROOT       = 'https://publicws.bzacd.com'
                                Exersise_ID   = Post.objects.raw(sql)
                                Exersise_ID1  = Post.objects.raw(sql1)
                                Exersise_ID2  = Post.objects.raw(sql2)
                                Exersise_ID3  = Post.objects.raw(sql3)
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total)
                                        json_res.append([json_obj])
                                        for record1 in Exersise_ID1:
                                                json_obj1 = dict(Easy  = record1.Easy)
                                                json_res.append([json_obj1])
                                                for record2 in Exersise_ID2:
                                                        json_obj2 = dict(Medium  = record2.Medium)
                                                        json_res.append([json_obj2])
                                                        for record3 in Exersise_ID3:
                                                                json_obj3 = dict(Hard  = record3.Hard)
                                                                json_res.append([json_obj3])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "select ple.id , count(*) as Total from Beezaccs_pr_link_exercises as ple where ple.user="+ID_user+" and ple.answer=ple.true_answer"
                                sql1          = "select ple.id , count(*) as Easy from Beezaccs_pr_link_exercises as ple inner join Beezaccs_pr_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_pr_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=1 and ple.answer=ple.true_answer"
                                sql2          = "select ple.id , count(*) as Medium from Beezaccs_pr_link_exercises as ple inner join Beezaccs_pr_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_pr_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=2 and ple.answer=ple.true_answer"
                                sql3          = "select ple.id , count(*) as Hard from Beezaccs_pr_link_exercises as ple inner join Beezaccs_pr_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_pr_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=3 and ple.answer=ple.true_answer"
                                URLROOT       = 'https://publicws.bzacd.com'
                                Exersise_ID   = Post.objects.raw(sql)
                                Exersise_ID1  = Post.objects.raw(sql1)
                                Exersise_ID2  = Post.objects.raw(sql2)
                                Exersise_ID3  = Post.objects.raw(sql3)
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total)
                                        json_res.append([json_obj])
                                        for record1 in Exersise_ID1:
                                                json_obj1 = dict(Easy  = record1.Easy)
                                                json_res.append([json_obj1])
                                                for record2 in Exersise_ID2:
                                                        json_obj2 = dict(Medium  = record2.Medium)
                                                        json_res.append([json_obj2])
                                                        for record3 in Exersise_ID3:
                                                                json_obj3 = dict(Hard  = record3.Hard)
                                                                json_res.append([json_obj3])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "select ple.id , count(*) as Total from Beezaccs_mid_link_exercises as ple where ple.user="+ID_user+" and ple.answer=ple.true_answer"
                                sql1          = "select ple.id , count(*) as Easy from Beezaccs_mid_link_exercises as ple inner join Beezaccs_mid_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_mid_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=1 and ple.answer=ple.true_answer"
                                sql2          = "select ple.id , count(*) as Medium from Beezaccs_mid_link_exercises as ple inner join Beezaccs_mid_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_mid_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=2 and ple.answer=ple.true_answer"
                                sql3          = "select ple.id , count(*) as Hard from Beezaccs_mid_link_exercises as ple inner join Beezaccs_mid_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_mid_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=3 and ple.answer=ple.true_answer"
                                URLROOT       = 'https://publicws.bzacd.com'
                                Exersise_ID   = Post.objects.raw(sql)
                                Exersise_ID1  = Post.objects.raw(sql1)
                                Exersise_ID2  = Post.objects.raw(sql2)
                                Exersise_ID3  = Post.objects.raw(sql3)
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total)
                                        json_res.append([json_obj])
                                        for record1 in Exersise_ID1:
                                                json_obj1 = dict(Easy  = record1.Easy)
                                                json_res.append([json_obj1])
                                                for record2 in Exersise_ID2:
                                                        json_obj2 = dict(Medium  = record2.Medium)
                                                        json_res.append([json_obj2])
                                                        for record3 in Exersise_ID3:
                                                                json_obj3 = dict(Hard  = record3.Hard)
                                                                json_res.append([json_obj3])
                                return Response({'Data':json_res})

# API To Return In Correct Answer Questions To User
class InCorrectAnswer(generics.GenericAPIView):
        def get(self , request , ID_user):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "select ple.id , count(*) as Total from Beezaccs_kin_linkexercises as ple where ple.user="+ID_user+" and ple.answer<>ple.true_answer"
                                sql1          = "select ple.id , count(*) as Easy from Beezaccs_kin_linkexercises as ple inner join Beezaccs_kin_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=1 and ple.answer<>ple.true_answer"
                                sql2          = "select ple.id , count(*) as Medium from Beezaccs_kin_linkexercises as ple inner join Beezaccs_kin_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=2 and ple.answer<>ple.true_answer"
                                sql3          = "select ple.id , count(*) as Hard from Beezaccs_kin_linkexercises as ple inner join Beezaccs_kin_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=3 and ple.answer<>ple.true_answer"
                                URLROOT       = 'https://publicws.bzacd.com'
                                Exersise_ID   = Post.objects.raw(sql)
                                Exersise_ID1  = Post.objects.raw(sql1)
                                Exersise_ID2  = Post.objects.raw(sql2)
                                Exersise_ID3  = Post.objects.raw(sql3)
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total)
                                        json_res.append([json_obj])
                                        for record1 in Exersise_ID1:
                                                json_obj1 = dict(Easy  = record1.Easy)
                                                json_res.append([json_obj1])
                                                for record2 in Exersise_ID2:
                                                        json_obj2 = dict(Medium  = record2.Medium)
                                                        json_res.append([json_obj2])
                                                        for record3 in Exersise_ID3:
                                                                json_obj3 = dict(Hard  = record3.Hard)
                                                                json_res.append([json_obj3])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "select ple.id , count(*) as Total from Beezaccs_pr_link_exercises as ple where ple.user="+ID_user+" and ple.answer<>ple.true_answer"
                                sql1          = "select ple.id , count(*) as Easy from Beezaccs_pr_link_exercises as ple inner join Beezaccs_pr_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_pr_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=1 and ple.answer<>ple.true_answer"
                                sql2          = "select ple.id , count(*) as Medium from Beezaccs_pr_link_exercises as ple inner join Beezaccs_pr_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_pr_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=2 and ple.answer<>ple.true_answer"
                                sql3          = "select ple.id , count(*) as Hard from Beezaccs_pr_link_exercises as ple inner join Beezaccs_pr_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_pr_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=3 and ple.answer<>ple.true_answer"
                                URLROOT       = 'https://publicws.bzacd.com'
                                Exersise_ID   = Post.objects.raw(sql)
                                Exersise_ID1  = Post.objects.raw(sql1)
                                Exersise_ID2  = Post.objects.raw(sql2)
                                Exersise_ID3  = Post.objects.raw(sql3)
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total)
                                        json_res.append([json_obj])
                                        for record1 in Exersise_ID1:
                                                json_obj1 = dict(Easy  = record1.Easy)
                                                json_res.append([json_obj1])
                                                for record2 in Exersise_ID2:
                                                        json_obj2 = dict(Medium  = record2.Medium)
                                                        json_res.append([json_obj2])
                                                        for record3 in Exersise_ID3:
                                                                json_obj3 = dict(Hard  = record3.Hard)
                                                                json_res.append([json_obj3])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "select ple.id , count(*) as Total from Beezaccs_mid_link_exercises as ple where ple.user="+ID_user+" and ple.answer<>ple.true_answer"
                                sql1          = "select ple.id , count(*) as Easy from Beezaccs_mid_link_exercises as ple inner join Beezaccs_mid_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_mid_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=1 and ple.answer<>ple.true_answer"
                                sql2          = "select ple.id , count(*) as Medium from Beezaccs_mid_link_exercises as ple inner join Beezaccs_mid_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_mid_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=2 and ple.answer<>ple.true_answer"
                                sql3          = "select ple.id , count(*) as Hard from Beezaccs_mid_link_exercises as ple inner join Beezaccs_mid_exercisesonline as bpe on ple.exercise=bpe.id INNER JOIN Beezaccs_mid_exersisetype as bpt on bpe.exercisetypy_id=bpt.id where ple.user="+ID_user+" and bpe.exercisetypy_id=3 and ple.answer<>ple.true_answer"
                                URLROOT       = 'https://publicws.bzacd.com'
                                Exersise_ID   = Post.objects.raw(sql)
                                Exersise_ID1  = Post.objects.raw(sql1)
                                Exersise_ID2  = Post.objects.raw(sql2)
                                Exersise_ID3  = Post.objects.raw(sql3)
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total)
                                        json_res.append([json_obj])
                                        for record1 in Exersise_ID1:
                                                json_obj1 = dict(Easy  = record1.Easy)
                                                json_res.append([json_obj1])
                                                for record2 in Exersise_ID2:
                                                        json_obj2 = dict(Medium  = record2.Medium)
                                                        json_res.append([json_obj2])
                                                        for record3 in Exersise_ID3:
                                                                json_obj3 = dict(Hard  = record3.Hard)
                                                                json_res.append([json_obj3])
                                return Response({'Data':json_res})

# API To Search Student Name
class ThSearchStudent(generics.GenericAPIView):
        def get(self , request , Name):
                json_res      = []
                for e in User.objects.filter(first_name__icontains=Name):
                        json_obj  = dict(IdStudent = e.id , FirstName = e.first_name , LastName = e.last_name)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Return Student class
class ThStudentClass(generics.GenericAPIView):
        def get(self , request , ID_user):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT bs.id , bs.kgclass_id , bc.classes FROM Beezaccs_studentclass as bs INNER JOIN Beezaccs_classes as bc WHERE bs.kgclass_id=bc.id and bs.student_id="+ID_user
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ClassID = record.kgclass_id , ClassName = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT bs.id , bs.prclass_id , bc.classes FROM Beezaccs_studentclass as bs INNER JOIN Beezaccs_pr_classes as bc WHERE bs.prclass_id=bc.id and bs.student_id="+ID_user
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ClassID = record.prclass_id , ClassName = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT bs.id , bs.midclass_id , bc.classes FROM Beezaccs_studentclass as bs INNER JOIN Beezaccs_mid_classes as bc WHERE bs.midclass_id=bc.id and bs.student_id="+ID_user;
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(ClassID = record.midclass_id , ClassName = record.classes)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Insert Student Section
class ThInsertStudentSection(generics.GenericAPIView):
        def post(self , request , ID_user , ID_class , ID_section , ID_subject , ID_student):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                student       = User.objects.get(id=ID_student)
                                level         = Level.objects.get(id=record.level_id)
                                classes       = Classes.objects.get(id=ID_class)
                                categories    = Kin_CategoriesClass.objects.get(id=ID_subject)
                                section       = Section.objects.get(id=ID_section)
                                StudentAssignment.objects.create(student=student,level=level,kgclass=classes,kgsubject=categories,Section=section)
                                return Response({'Data':'Successfully Added'})
                        if (record.level_id==2):
                                student       = User.objects.get(id=ID_student)
                                level         = Level.objects.get(id=record.level_id)
                                classes       = Pr_Classes.objects.get(id=ID_class)
                                categories    = Pr_Subject.objects.get(id=ID_subject)
                                section       = Section.objects.get(id=ID_section)
                                StudentAssignment.objects.create(student=student,level=level,prclass=classes,prsubject=categories,Section=section)
                                return Response({'Data':'Successfully Added'})
                        else:
                                student       = User.objects.get(id=ID_student)
                                level         = Level.objects.get(id=record.level_id)
                                classes       = Mid_Classes.objects.get(id=ID_class)
                                categories    = Mid_Subject.objects.get(id=ID_subject)
                                section       = Section.objects.get(id=ID_section)
                                StudentAssignment.objects.create(student=student,level=level,midclass=classes,midsubject=categories,Section=section)
                                return Response({'Data':'Successfully Added'})

# API To Delete Student Section
class ThDeleteStudentSection(generics.GenericAPIView):
        def get(self , request , ID_user , ID_class , ID_section , ID_subject , ID_student):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                student       = User.objects.get(id=ID_student)
                                level         = Level.objects.get(id=record.level_id)
                                classes       = Classes.objects.get(id=ID_class)
                                categories    = Kin_CategoriesClass.objects.get(id=ID_subject)
                                section       = Section.objects.get(id=ID_section)
                                StudentAssignment.objects.filter(student=student,level=level,kgclass=classes,kgsubject=categories,Section=section).delete()
                                return Response({'Data':'Successfully Delete'})
                        if (record.level_id==2):
                                student       = User.objects.get(id=ID_student)
                                level         = Level.objects.get(id=record.level_id)
                                classes       = Pr_Classes.objects.get(id=ID_class)
                                categories    = Pr_Subject.objects.get(id=ID_subject)
                                section       = Section.objects.get(id=ID_section)
                                StudentAssignment.objects.filter(student=student,level=level,prclass=classes,prsubject=categories,Section=section).delete()
                                return Response({'Data':'Successfully Delete'})
                        else:
                                student       = User.objects.get(id=ID_student)
                                level         = Level.objects.get(id=record.level_id)
                                classes       = Mid_Classes.objects.get(id=ID_class)
                                categories    = Mid_Subject.objects.get(id=ID_subject)
                                section       = Section.objects.get(id=ID_section)
                                StudentAssignment.objects.filter(student=student,level=level,midclass=classes,midsubject=categories,Section=section).delete()
                                return Response({'Data':'Successfully Delete'})
                
# API To Return Total Student class
class ThTotalStudent(generics.GenericAPIView):
        def get(self , request , ID_user , ID_class , ID_section , ID_subject):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT id , COUNT(DISTINCT student_id) as TotalStudent FROM Beezaccs_studentassignment WHERE level_id=1 AND kgclass_id="+ID_class+" AND Section_id="+ID_section+" AND kgsubject_id="+ID_subject
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(TotalStudent=record.TotalStudent)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT id , COUNT(DISTINCT student_id) as TotalStudent FROM Beezaccs_studentassignment WHERE level_id=2 AND prclass_id="+ID_class+"  AND Section_id="+ID_section+" AND prsubject_id="+ID_subject
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(TotalStudent=record.TotalStudent)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT id , COUNT(DISTINCT student_id) as TotalStudent FROM Beezaccs_studentassignment WHERE level_id=3 AND midclass_id=="+ID_class+" AND Section_id="+ID_section+" AND midsubject_id="+ID_subject
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(TotalStudent=record.TotalStudent)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return Total Assignment IN class
class ThTotalAssignmentStudent(generics.GenericAPIView):
        def get(self , request , ID_user , ID_class , ID_section , ID_subject):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT id , COUNT(*) as TotalAssignment FROM Beezaccs_studentassignment WHERE level_id=1 AND kgclass_id="+ID_class+"  AND Section_id="+ID_section+" AND kgsubject_id="+ID_subject+" AND AssignmentType_id=1"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(TotalAssignment=record.TotalAssignment)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT id , COUNT(*) as TotalAssignment FROM Beezaccs_studentassignment WHERE level_id=2 AND prclass_id="+ID_class+"  AND Section_id="+ID_section+" AND prsubject_id="+ID_subject+" AND AssignmentType_id=1"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(TotalAssignment=record.TotalAssignment)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT id , COUNT(*) as TotalAssignment FROM Beezaccs_studentassignment WHERE level_id=3 AND midclass_id=="+ID_class+" AND Section_id="+ID_section+" AND midsubject_id="+ID_subject+" AND AssignmentType_id=1"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(TotalAssignment=record.TotalAssignment)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return Total Exam IN class
class ThTotalExamStudent(generics.GenericAPIView):
        def get(self , request , ID_user , ID_class , ID_section , ID_subject):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT id , COUNT(*) as TotalExam FROM Beezaccs_studentassignment WHERE level_id=1 AND kgclass_id="+ID_class+"  AND Section_id="+ID_section+" AND kgsubject_id="+ID_subject+" AND AssignmentType_id=2"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(TotalExam=record.TotalExam)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT id , COUNT(*) as TotalExam FROM Beezaccs_studentassignment WHERE level_id=2 AND prclass_id="+ID_class+"  AND Section_id="+ID_section+" AND prsubject_id="+ID_subject+" AND AssignmentType_id=2"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(TotalExam=record.TotalExam)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT id , COUNT(*) as TotalExam FROM Beezaccs_studentassignment WHERE level_id=3 AND midclass_id="+ID_class+" AND Section_id="+ID_section+" AND midsubject_id="+ID_subject+" AND AssignmentType_id=2"
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(TotalExam=record.TotalExam)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return All Student class
class ThAllStudent(generics.GenericAPIView):
        def get(self , request , ID_user , ID_class , ID_section , ID_subject):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT DISTINCT bs.student_id as id , au.first_name , au.last_name FROM Beezaccs_studentassignment AS bs INNER JOIN accounts_user as au on bs.student_id=au.id WHERE level_id=1 AND kgclass_id="+ID_class+" AND Section_id="+ID_section+" AND kgsubject_id="+ID_subject
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(StudentID = record.id , FirstName = record.first_name , LastName = record.last_name)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT DISTINCT bs.student_id , au.first_name , au.last_name FROM Beezaccs_studentassignment AS bs INNER JOIN accounts_user as au on bs.student_id=au.id WHERE level_id=2 AND prclass_id="+ID_class+" AND Section_id="+ID_section+" AND prsubject_id="+ID_subject
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(StudentID = record.id , FirstName = record.first_name , LastName = record.last_name)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT DISTINCT bs.student_id , au.first_name , au.last_name FROM Beezaccs_studentassignment AS bs INNER JOIN accounts_user as au on bs.student_id=au.id WHERE level_id=3 AND midclass_id="+ID_class+" AND Section_id="+ID_section+" AND midsubject_id="+ID_subject
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = json_obj  = dict(TotalStudent=record.TotalStudent)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Return Count exersise To Student class
class ThCountExersisesStudent(generics.GenericAPIView):
        def get(self , request , ID_user , ID_class , ID_subject):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                json_res      = []
                                sql           = "SELECT bke.id , COUNT(*) as Total FROM Beezaccs_kin_exercisesonline as bke INNER JOIN Beezaccs_kin_linkexercises AS bkl on bke.id=bkl.exercise WHERE bke.level_id=1 AND bke.classes_id="+ID_class+" AND bke.categories_id="+ID_subject+" AND bkl.user="+ID_user
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        if (record.level_id==2):
                                json_res      = []
                                sql           = "SELECT bke.id , COUNT(*) as Total FROM Beezaccs_pr_exercisesonline as bke INNER JOIN beezaccs_pr_link_exercises AS bkl on bke.id=bkl.exercise WHERE bke.level_id=2 AND bke.classes_id="+ID_class+" AND bke.subject_id="+ID_subject+" AND bkl.user="+ID_user
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})
                        else:
                                json_res      = []
                                sql           = "SELECT bke.id , COUNT(*) as Total FROM Beezaccs_mid_exercisesonline as bke INNER JOIN beezaccs_mid_link_exercises AS bkl on bke.id=bkl.exercise WHERE bke.level_id=3 AND bke.classes_id="+ID_class+" AND bke.subject_id="+ID_subject+" AND bkl.user="+ID_user
                                Exersise_ID   = StudentSchoole.objects.raw(sql)
                                URLROOT       = 'https://publicws.bzacd.com'
                                for record in Exersise_ID:
                                        json_obj  = dict(Total = record.Total)
                                        json_res.append([json_obj])
                                return Response({'Data':json_res})

# API To Teacher Create New Post
class ThCreatePost(generics.GenericAPIView):
        def post(self , request , ID_user , post , ImagePost):
                user          = User.objects.get(id=ID_user)
                Post.objects.create(user=user,post=post,image=ImagePost)
                return Response({'Data':'Successfully Added'})

# API To Student Create New Post
class StCreatePost(generics.GenericAPIView):
        def post(self , request , ID_user , post , ImagePost):
                user          = User.objects.get(id=ID_user)
                Post.objects.create(user=user,post=post,image=ImagePost)
                return Response({'Data':'Successfully Added'})

# API To Return ID Children About Parent
class PrChildrenID(generics.GenericAPIView):
        def get(self , request , ID_user):
                json_res      = []
                sql           = "select id , Student_ID_id from Beezaccs_parent where Parent_ID_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        json_obj  = dict(StudentId = record.Student_ID_id)
                        json_res.append([json_obj])
                return Response({'Data':json_res})

# API To Insert Assignment About Parent
class PrInsertAssignment(generics.GenericAPIView):
        def post(self , request , ID_user , ID_student , ID_pro_Type , ID_class , ID_section , ID_subject , ID_unit , ID_topic , ID_type , submissiondate , ID_duration):
                json_res      = []
                sql           = "select id , level_id from Beezaccs_studentclass where student_id="+ID_user
                Exersise_ID   = Pr_ExercisesOnline.objects.raw(sql)
                for record in Exersise_ID:
                        if (record.level_id==1):
                                student       = User.objects.get(id=ID_student)
                                level         = Level.objects.get(id=record.level_id)
                                procedure     = Procedure.objects.get(id=ID_pro_Type)
                                classes       = Classes.objects.get(id=ID_class)
                                categories    = Kin_CategoriesClass.objects.get(id=ID_subject)
                                topic         = Topic.objects.get(id=ID_unit)
                                sub_topic     = Sub_Topic.objects.get(id=ID_topic)
                                topictypy     = TopicType.objects.get(id=ID_type)
                                duration      = DurationTime.objects.get(id=ID_duration)
                                section       = Section.objects.get(id=ID_section)
                                StudentAssignment.objects.create(student=student,level=level,kgclass=classes,kgsubject=categories,kguint=topic,kgtopic=sub_topic,AssignmentType=procedure,TopicType=topictypy,Section=section,DurationTime=duration,submissionDate=submissiondate)
                                return Response({'Data':'Successfully Added'})
                        if (record.level_id==2):
                                student       = User.objects.get(id=ID_user)
                                level         = Level.objects.get(id=record.level_id)
                                procedure     = Procedure.objects.get(id=ID_pro_Type)
                                classes       = Pr_Classes.objects.get(id=ID_class)
                                categories    = Pr_Subject.objects.get(id=ID_subject)
                                topic         = Pr_Uint.objects.get(id=ID_unit)
                                sub_topic     = Pr_Topic.objects.get(id=ID_topic)
                                topictypy     = Pr_ExersiseType.objects.get(id=ID_type)
                                duration      = Pr_is_True.objects.get(id=ID_duration)
                                section       = Section.objects.get(id=ID_correct)
                                StudentAssignment.objects.create(student=student,level=level,prclass=classes,prsubject=categories,pruint=topic,prtopic=sub_topic,AssignmentType=procedure,TopicType=topictypy,Section=section,DurationTime=duration,submissionDate=submissiondate)
                                return Response({'Data':'Successfully Added'})
                        else:
                                student       = User.objects.get(id=ID_user)
                                level         = Level.objects.get(id=record.level_id)
                                procedure     = Procedure.objects.get(id=ID_pro_Type)
                                classes       = Mid_Classes.objects.get(id=ID_class)
                                categories    = Mid_Subject.objects.get(id=ID_subject)
                                topic         = Mid_Uint.objects.get(id=ID_unit)
                                sub_topic     = Mid_Topic.objects.get(id=ID_topic)
                                topictypy     = Mid_ExersiseType.objects.get(id=ID_type)
                                duration      = Mid_is_True.objects.get(id=ID_duration)
                                section       = Section.objects.get(id=ID_correct)
                                StudentAssignment.objects.create(student=student,level=level,midclass=classes,midsubject=categories,mduint=topic,mdtopic=sub_topic,AssignmentType=procedure,TopicType=topictypy,Section=section,DurationTime=duration,submissionDate=submissiondate)
                                return Response({'Data':'Successfully Added'})

# # API To Create New Chat
# class CreateChatSessionView(generics.GenericAPIView):
#         def post(self, request, ID_user):
#                 user = User.objects.get(id=ID_user)
#                 chat_session = ChatSession.objects.create(owner=user)
#                 return Response({'status': 'SUCCESS', 'uri': chat_session.uri,'message': 'New chat session created'})

# # API To Add User To Chat
# class UserChatSessionView(generics.GenericAPIView):
#         def patch(self, request, ID_user , uri):
#                 User = get_user_model()
#                 URI = uri
#                 user = User.objects.get(id=ID_user)
#                 chat_session = ChatSession.objects.get(uri=URI)
#                 owner = chat_session.owner
#                 if owner != user:               
#                         chat_session.members.get_or_create(user=user, chat_session=chat_session)
#                 owner = deserialize_user(owner)
#                 members = [
#                 deserialize_user(chat_session.user) 
#                 for chat_session in chat_session.members.all()
#                 ]
#                 members.insert(0, owner)
#                 return Response ({
#                 'status': 'SUCCESS', 'members': members,
#                 'message': '%s joined the chat' % user.username,
#                 'user': deserialize_user(user)
#                 })

# # API To Get All Message
# class MessageGetChatView(generics.GenericAPIView):
#     def get(self, request, uri):
#         URI = uri

#         chat_session = ChatSession.objects.get(uri=URI)
#         messages = [chat_session_message.to_json() 
#             for chat_session_message in chat_session.messages.all()]

#         return Response({
#             'id': chat_session.id, 'uri': chat_session.uri,
#             'messages': messages
#         })

# # API To Create Message
# class MessagePostChatView(generics.GenericAPIView):
#     def post(self, request, ID_user , uri , message):
#         URI = uri
#         MESSAGE = message
#         user = User.objects.get(id=ID_user)
#         chat_session = ChatSession.objects.get(uri=uri)

#         chat_session_message = ChatSessionMessage.objects.create(
#             user=user, chat_session=chat_session, message=message
#         )

#         notif_args = {
#             'source': user,
#             'source_display_name': user.get_full_name(),
#             'category': 'chat', 'action': 'Sent',
#             'obj': chat_session_message.id,
#             'short_description': 'You a new message', 'silent': True,
#             'extra_data': {'uri': chat_session.uri}
#         }
#         notify.send(
#             sender=self.__class__, **notif_args, channels=['websocket']
#         )

#         return Response ({
#             'status': 'SUCCESS', 'uri': chat_session.uri, 'message': message,
#             'user': deserialize_user(user)
#         })

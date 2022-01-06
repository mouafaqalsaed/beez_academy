from django.db import models
from accounts.models import User
# from django.contrib.auth.models import User
import os
from ckeditor.fields import RichTextField
from uuid import uuid4

from django.db import models
from django.contrib.auth import get_user_model

# Get File
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    justname = filename.split('.')[0]
    filename = "%s.%s" % (justname, ext)
    return os.path.join('static/images/profile/', filename)
#PHASE01
# 001_Table Categories
class Categories(models.Model):
    CATEGORY=(
        ('Alphabet-Arabic','Alphabet-Arabic'),
        ('Math','Math'),
        ('Maze','Maze'),
        ('FollowDot','FollowDot'),
        ('Alphabet-English','Alphabet-English'),
        ('Alphabet-French','Alphabet-French')
    )
    category      = models.CharField(max_length=190,null=True,choices=CATEGORY)
    date_created  = models.DateTimeField(auto_now_add=True,null=True)
    image         = models.FileField(upload_to='static',null=True)
    def __str__(self):
        return self.category

# 002_Table Exercises
class Exercises(models.Model):
    categories    = models.ForeignKey(Categories,null=True,on_delete=models.SET_NULL,related_name="exercises")
    description   = models.CharField(max_length=190,null=True)
    date_created  = models.DateTimeField(auto_now_add=True,null=True)
    File          = models.FileField(upload_to='static',null=True)
    image         = models.FileField(upload_to='static',null=True)
    alphabet_id   = models.CharField(max_length=190,null=True)
    def __str__(self):
        return self.description
        
# 003_Table ContactUs
class ContactUs(models.Model):
    name          = models.CharField(max_length=190,null=True)
    email         = models.CharField(max_length=190,null=True)
    country       = models.CharField(max_length=190,null=True)
    message       = models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.name

# PHASE02
# Kindergarten
# 001_Table Category_Type
class Kin_CategoryType(models.Model):
    NAME=(
        ('Offline','Offline'),
        ('Online','Online'),
    )
    name              = models.CharField(unique=True,max_length=190,null=True,choices=NAME)
    date_created      = models.DateTimeField(auto_now_add=True,null=True)
    date_updated      = models.DateTimeField(auto_now=True)
    image             = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image = models.CharField(max_length=190,null=True,default='image')
    def __str__(self):
        return self.name

# 002_Table Categories_Offline
class CategoriesOffline(models.Model):
    CATEGORY=(
        ('Alphabet','Alphabet'),
        ('Math','Math'),
        ('Creativity','Creativity')
    )
    category          = models.CharField(unique=True,max_length=190,null=True,choices=CATEGORY)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    image             = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image = models.CharField(max_length=190,null=True,blank=True)
    def __str__(self):
        return self.category

# 003_Table Categories_Class
class Kin_CategoriesClass(models.Model):
    CATEGORY=(
        ('Literacy','Literacy'),
        ('Math','Math'),
        ('Creativity','Creativity'),
    )
    category          = models.CharField(unique=True,max_length=190,null=True,choices=CATEGORY)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    image             = models.FileField(upload_to='static', null=True,blank=True)
    alternative_image = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.category

# 004_Table Level
class Level(models.Model):
    LEVEL=(
        ('Kindergarten','Kindergarten'),
        ('Primary','Primary'),
        ('Middle','Middle'),
        ('Secondary','Secondary')
    )
    level             = models.CharField(unique=True,max_length=190,null=True,choices=LEVEL)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    description       = models.CharField(max_length=190,null=True)
    image             = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.level

# 005_Table ExercisesOffline
class Classes(models.Model):
    CLASSES=(
        ('Pre-KG','Pre-KG'),
        ('KG-1','KG-1'),
        ('KG-2','KG-2'),
    )
    classes           = models.CharField(unique=True,max_length=190,null=True,choices=CLASSES)
    level             = models.ForeignKey(Level,null=True,on_delete=models.SET_NULL,related_name="classes")
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    image             = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.classes

# 006_Table ExercisesOffline
class Kin_ExercisesOffline(models.Model):
    categories        = models.ForeignKey(CategoriesOffline,null=True,on_delete=models.SET_NULL,related_name="categories")
    level             = models.ForeignKey(Level,null=True,on_delete=models.SET_NULL,related_name="level1")
    classes           = models.ForeignKey(Classes,null=True,on_delete=models.SET_NULL,related_name="classes1")
    exercise          = models.CharField(unique=True,max_length=190,null=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    File              = models.FileField(upload_to='static',null=True,blank=True)
    image             = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.exercise

# 007_Table ExersiseType
class ExersiseType(models.Model):
    ExerciseTypy  = (
        ('Hard','Hard'),
        ('Medium','Medium'),
        ('Easy','Easy')
    )   
    exercisetypy      = models.CharField(unique=True,max_length=190,null=True,choices=ExerciseTypy)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    image             = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.exercisetypy

# 008_Table Topics
class Topic(models.Model):
    Topic      = models.CharField(max_length=190,null=True)
    def __str__(self):
        return self.Topic

# 009_Table Suc_Topics
class Sub_Topic(models.Model):
    Sub_Topic      = models.CharField(max_length=190,null=True)
    def __str__(self):
        return self.Sub_Topic

# 010_Table Link_Topic
class Link_Topic(models.Model):
    name          = models.CharField(max_length=190,null=True)
    topic         = models.ForeignKey(Topic,null=True,on_delete=models.SET_NULL,related_name="topics")
    classes       = models.ForeignKey(Classes,null=True,on_delete=models.SET_NULL,related_name="classesss")
    categories    = models.ForeignKey(Kin_CategoriesClass,null=True,on_delete=models.SET_NULL,related_name="categoriess")
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    image         = models.FileField(upload_to='static',null=True,blank=True)
    def __str__(self):
        return self.name

# 011_Table Link_Sub_Topic
class Link_Sub_Topic(models.Model):
    name          = models.CharField(max_length=190,null=True)
    sub_topic     = models.ForeignKey(Sub_Topic,null=True,on_delete=models.SET_NULL,related_name="subtopics")
    topic         = models.ForeignKey(Topic,null=True,on_delete=models.SET_NULL,related_name="topic")
    class_name    = models.ForeignKey(Classes,null=True,on_delete=models.SET_NULL,related_name="classes2")
    categories    = models.ForeignKey(Kin_CategoriesClass,null=True,on_delete=models.SET_NULL,related_name="categories1")
    image         = models.FileField(upload_to='static',null=True,blank=True)
    def __str__(self):
        return self.name

# 012_Table is_True
class is_True(models.Model):
    ISTRUE  = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
        ('A_Image','A_Image'),
        ('B_Image','B_Image'),
        ('C_Image','C_Image'),
        ('D_Image','D_Image'),
    )   
    istrue        = models.CharField(max_length=190,null=True,choices=ISTRUE)
    def __str__(self):
        return self.istrue

# 013_Table Kin_ExercisesOnline
class Kin_ExercisesOnline(models.Model):
    level               = models.ForeignKey(Level,null=True,on_delete=models.SET_NULL,related_name="levels")
    classes             = models.ForeignKey(Classes,null=True,on_delete=models.SET_NULL,related_name="classess")
    categories          = models.ForeignKey(Kin_CategoriesClass,null=True,on_delete=models.SET_NULL,related_name="categories")
    topic               = models.ForeignKey(Topic,null=True,on_delete=models.SET_NULL,related_name="topics1")
    sub_topic           = models.ForeignKey(Sub_Topic,null=True,on_delete=models.SET_NULL,related_name="subtopics1")
    exercisetypy        = models.ForeignKey(ExersiseType,null=True,on_delete=models.SET_NULL,related_name="exercisetypys")
    exercise            = RichTextField(blank=True, null=True)
    is_Done             = models.BooleanField(default=False)
    is_Free             = models.BooleanField(default=True)
    is_True             = models.ForeignKey(is_True,null=True,on_delete=models.SET_NULL,related_name="istrues")
    A                   = models.CharField(max_length=190,null=True,blank=True)
    B                   = models.CharField(max_length=190,null=True,blank=True)
    C                   = models.CharField(max_length=190,null=True,blank=True)
    D                   = models.CharField(max_length=190,null=True,blank=True)
    A_Image             = models.FileField(default="/" , upload_to='static',null=True,blank=True)
    alternative_A_Image = models.CharField(max_length=190,null=True,blank=True,default='image')
    B_Image             = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    alternative_B_Image = models.CharField(max_length=190,null=True,blank=True,default='image')
    C_Image             = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    alternative_C_Image = models.CharField(max_length=190,null=True,blank=True,default='image')
    D_Image             = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    alternative_D_Image = models.CharField(max_length=190,null=True,blank=True,default='image')
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    File                = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    image               = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    alternative_image   = models.CharField(max_length=190,null=True,blank=True)
    explanation         = models.CharField(max_length=190,null=True,blank=True)
    def __str__(self):
        return self.exercise

# 014_Table Link_Exercises
class Kin_LinkExercises(models.Model):
    user          = models.CharField(max_length=190,null=True)
    exercise      = models.CharField(max_length=190,null=True)
    duration_Time = models.TimeField()
    answer        = models.CharField(max_length=190,null=True)
    true_answer   = models.CharField(max_length=190,null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.exercise

# 015_Table certificate
class Kin_Certificate(models.Model):
    Certificate_Title   = models.CharField(max_length=190,null=True)
    Certificate         = models.TextField(max_length=2500,null=True)
    topic               = models.ForeignKey(Topic,null=True,on_delete=models.SET_NULL,related_name="topics2")
    sub_topic           = models.ForeignKey(Sub_Topic,null=True,on_delete=models.SET_NULL,related_name="subtopics2")
    image               = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image   = models.CharField(max_length=190,null=True,blank=True,default='image')
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Certificate_Title

# 016_Table Link_certificate
class Kin_Link_Certificate(models.Model):
    user              = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="Users1")
    certificate       = models.ForeignKey(Kin_Certificate,null=True,on_delete=models.SET_NULL,related_name="certificate1")
    topic             = models.ForeignKey(Topic,null=True,on_delete=models.SET_NULL,related_name="topics3")
    sub_topic         = models.ForeignKey(Sub_Topic,null=True,on_delete=models.SET_NULL,related_name="subtopics3")
    duration_Time     = models.TimeField()
    image             = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image = models.CharField(max_length=190,null=True,blank=True,default='image')
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    # duration_Time     = models.TimeField()

# PHASE02
# Primary
# 017_Table PR_Classes
class Pr_Classes(models.Model):
    CLASSES=(
        ('Grade 1','Grade 1'),
        ('Grade 2','Grade 2'),
        ('Grade 3','Grade 3'),
        ('Grade 4','Grade 4'),
        ('Grade 5','Grade 5'),
        ('Grade 6','Grade 6'),
    )
    classes             = models.CharField(unique=True,max_length=190,null=True,choices=CLASSES)
    level               = models.ForeignKey(Level,null=True,on_delete=models.SET_NULL,related_name="PR_classes")
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    image               = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image   = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.classes

# 018_Table PR_Categories_Class
class Pr_Subject(models.Model):
    subject             = models.CharField(max_length=190,null=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    image               = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image   = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.subject

# 019_Table PR_Uints
class Pr_Uint(models.Model):
    Uint       = models.CharField(max_length=190,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Uint

# 020_Table PR_Topics
class Pr_Topic(models.Model):
    Topic      = models.CharField(unique=True,max_length=190,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Topic

# 021_Table PR_Summary
class Pr_Summary(models.Model):
    subject             = models.CharField(max_length=190,null=True,blank=True)
    # Text              = models.TextField(max_length=2500,null=True)
    Text                = RichTextField(blank=True, null=True)
    topic               = models.ForeignKey(Pr_Topic,null=True,on_delete=models.SET_NULL,related_name="subtopics04")
    image01             = models.FileField(default="/" ,upload_to='static', null=True,blank=True)
    alternative_image01 = models.CharField(max_length=190,null=True,blank=True,default='image')
    image02             = models.FileField(default="/" ,upload_to='static', null=True,blank=True)
    alternative_image02 = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.subject

# 022_Table PR_ExersiseType
class Pr_ExersiseType(models.Model):
    ExerciseTypy  = (
        ('Hard','Hard'),
        ('Medium','Medium'),
        ('Easy','Easy')
    )   
    exercisetypy      = models.CharField(unique=True,max_length=190,null=True,choices=ExerciseTypy)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    image             = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.exercisetypy

# 023_Table is_True
class Pr_is_True(models.Model):
    ISTRUE  = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
        ('A_Image','A_Image'),
        ('B_Image','B_Image'),
        ('C_Image','C_Image'),
        ('D_Image','D_Image'),
    )   
    istrue        = models.CharField(max_length=190,null=True,choices=ISTRUE)
    def __str__(self):
        return self.istrue

# 024_Table PR_Link_Topic
class Pr_Link_Topic(models.Model):
    uint              = models.ForeignKey(Pr_Uint,null=True,on_delete=models.SET_NULL,related_name="pr_topics")
    classes           = models.ForeignKey(Pr_Classes,null=True,on_delete=models.SET_NULL,related_name="pr_classesss")
    subject           = models.ForeignKey(Pr_Subject,null=True,on_delete=models.SET_NULL,related_name="pr_categoriess")
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    image             = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.topic

# 025_Table PR_Link_Sub_Topic
class Pr_Link_Sub_Topic(models.Model):
    topic         = models.ForeignKey(Pr_Topic,null=True,on_delete=models.SET_NULL,related_name="subtopics")
    uint          = models.ForeignKey(Pr_Uint,null=True,on_delete=models.SET_NULL,related_name="topic")
    class_name    = models.ForeignKey(Pr_Classes,null=True,on_delete=models.SET_NULL,related_name="classes2")
    subject       = models.ForeignKey(Pr_Subject,null=True,on_delete=models.SET_NULL,related_name="categories1")
    image         = models.FileField(upload_to='static',null=True,blank=True)
    def __str__(self):
        return self.sub_topic

# 026_Table ExercisesOnline
class Pr_ExercisesOnline(models.Model):
    level               = models.ForeignKey(Level,null=True,on_delete=models.SET_NULL,related_name="levels03")
    classes             = models.ForeignKey(Pr_Classes,null=True,on_delete=models.SET_NULL,related_name="classess03")
    subject             = models.ForeignKey(Pr_Subject,null=True,on_delete=models.SET_NULL,related_name="categories03")
    unit                = models.ForeignKey(Pr_Uint,null=True,on_delete=models.SET_NULL,related_name="topics03")
    topic               = models.ForeignKey(Pr_Topic,null=True,on_delete=models.SET_NULL,related_name="subtopics03")
    exercisetypy        = models.ForeignKey(Pr_ExersiseType,null=True,on_delete=models.SET_NULL,related_name="exercisetypys03")
    exercise            = RichTextField(blank=True, null=True)
    # exercise          = models.CharField(max_length=190,null=True)
    is_Done             = models.BooleanField(default=False)
    is_Free             = models.BooleanField(default=True)
    is_True             = models.ForeignKey(Pr_is_True,null=True,on_delete=models.SET_NULL,related_name="istrues03")
    A                   = models.CharField(max_length=190,null=True,blank=True)
    B                   = models.CharField(max_length=190,null=True,blank=True)
    C                   = models.CharField(max_length=190,null=True,blank=True)
    D                   = models.CharField(max_length=190,null=True,blank=True)
    A_Image             = models.FileField(default="/" , upload_to='static',null=True,blank=True)
    alternative_A_Image = models.CharField(max_length=190,null=True,blank=True,default='image')
    B_Image             = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    alternative_B_Image = models.CharField(max_length=190,null=True,blank=True,default='image')
    C_Image             = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    alternative_C_Image = models.CharField(max_length=190,null=True,blank=True,default='image')
    D_Image             = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    alternative_D_Image = models.CharField(max_length=190,null=True,blank=True,default='image')
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    File                = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    image               = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    alternative_image   = models.CharField(max_length=190,null=True,blank=True)
    explanation         = models.CharField(max_length=190,null=True,blank=True)
    def __str__(self):
        return self.exercise

# 027_Table Link_Exercises
class Pr_Link_Exercises(models.Model):
    user          = models.CharField(max_length=190,null=True)
    exercise      = models.CharField(max_length=190,null=True)
    duration_Time = models.TimeField()
    answer        = models.CharField(max_length=190,null=True)
    true_answer   = models.CharField(max_length=190,null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.exercise

# 028_Table certificate
class Pr_Certificate(models.Model):
    Certificate_Title   = models.CharField(max_length=190,null=True)
    Certificate         = models.TextField(max_length=2500,null=True)
    topic               = models.ForeignKey(Pr_Topic,null=True,on_delete=models.SET_NULL,related_name="prtopic")
    unit                = models.ForeignKey(Pr_Uint,null=True,on_delete=models.SET_NULL,related_name="prunit")
    image               = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image   = models.CharField(max_length=190,null=True,blank=True,default='image')
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Certificate_Title

# 029_Table Link_certificate
class Pr_Link_Certificate(models.Model):
    user                = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="prUsers")
    certificate         = models.ForeignKey(Pr_Certificate,null=True,on_delete=models.SET_NULL,related_name="prcertificate")
    topic               = models.ForeignKey(Pr_Topic,null=True,on_delete=models.SET_NULL,related_name="prtopic1")
    unit                = models.ForeignKey(Pr_Uint,null=True,on_delete=models.SET_NULL,related_name="prunit1")
    duration_Time       = models.TimeField()
    image               = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image   = models.CharField(max_length=190,null=True,blank=True,default='image')
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    duration_Time       = models.TimeField()

# PHASE02
# Middle 
# 030_Table Mid_Classes
class Mid_Classes(models.Model):
    CLASSES=(
        ('Grade 7','Grade 7'),
        ('Grade 8','Grade 8'),
        ('Grade 9','Grade 9'),
    )
    classes             = models.CharField(unique=True,max_length=190,null=True,choices=CLASSES)
    level               = models.ForeignKey(Level,null=True,on_delete=models.SET_NULL,related_name="Mid_classes")
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    image               = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image   = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.classes

# 031_Table Mid_Categories_Class
class Mid_Subject(models.Model):
    subject             = models.CharField(max_length=190,null=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    image               = models.FileField(upload_to='static', null=True,blank=True)
    alternative_image   = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.subject

# 032_Table Mid_Uints
class Mid_Uint(models.Model):
    Uint      = models.CharField(max_length=190,null=True)
    def __str__(self):
        return self.Uint

# 033_Table Mid_Topics
class Mid_Topic(models.Model):
    Topic      = models.CharField(max_length=190,null=True)
    def __str__(self):
        return self.Topic

# 034_Table Mid_Summary
class Mid_Summary(models.Model):
    subject               = models.CharField(max_length=190,null=True,blank=True)
    Text                  = models.TextField(max_length=2500,null=True)
    topic                 = models.ForeignKey(Mid_Topic,null=True,on_delete=models.SET_NULL,related_name="Mid_subtopics")
    image01               = models.FileField(default="/" ,upload_to='static', null=True,blank=True)
    alternative_image01   = models.CharField(max_length=190,null=True,blank=True,default='image')
    image02               = models.FileField(default="/" ,upload_to='static', null=True,blank=True)
    alternative_image02   = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.subject

# 035_Table Mid_ExersiseType
class Mid_ExersiseType(models.Model):
    ExerciseTypy  = (
        ('Hard','Hard'),
        ('Medium','Medium'),
        ('Easy','Easy')
    )   
    exercisetypy      = models.CharField(unique=True,max_length=190,null=True,choices=ExerciseTypy)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    image             = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.exercisetypy

# 036_Table Mid_is_True
class Mid_is_True(models.Model):
    ISTRUE  = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
        ('A_Image','A_Image'),
        ('B_Image','B_Image'),
        ('C_Image','C_Image'),
        ('D_Image','D_Image'),
    )   
    istrue        = models.CharField(max_length=190,null=True,choices=ISTRUE)
    def __str__(self):
        return self.istrue

# 037_Table Mid_Link_Topic
class Mid_Link_Topic(models.Model):
    uint          = models.ForeignKey(Mid_Uint,null=True,on_delete=models.SET_NULL,related_name="Mid_topics")
    classes       = models.ForeignKey(Mid_Classes,null=True,on_delete=models.SET_NULL,related_name="Mid_classesss")
    subject       = models.ForeignKey(Mid_Subject,null=True,on_delete=models.SET_NULL,related_name="Mid_categoriess")
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    image         = models.FileField(upload_to='static',null=True,blank=True)
    def __str__(self):
        return self.uint

# 038_Table Mid_Link_Sub_Topic
class Mid_Link_Sub_Topic(models.Model):
    topic               = models.ForeignKey(Mid_Topic,null=True,on_delete=models.SET_NULL,related_name="Mid_subtopics2")
    uint          = models.ForeignKey(Mid_Uint,null=True,on_delete=models.SET_NULL,related_name="Mid_topic2")
    class_name    = models.ForeignKey(Mid_Classes,null=True,on_delete=models.SET_NULL,related_name="Mid_classes2")
    subject       = models.ForeignKey(Mid_Subject,null=True,on_delete=models.SET_NULL,related_name="Mid_categories2")
    image                 = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image01   = models.CharField(max_length=190,null=True,blank=True,default='image')
    def __str__(self):
        return self.topic

# 039_Table Mid_ExercisesOnline
class Mid_ExercisesOnline(models.Model):
    level               = models.ForeignKey(Level,null=True,on_delete=models.SET_NULL,related_name="Mid_levels03")
    classes             = models.ForeignKey(Mid_Classes,null=True,on_delete=models.SET_NULL,related_name="Mid_classess03")
    subject             = models.ForeignKey(Mid_Subject,null=True,on_delete=models.SET_NULL,related_name="Mid_categories03")
    unit                = models.ForeignKey(Mid_Uint,null=True,on_delete=models.SET_NULL,related_name="Mid_topics03")
    topic               = models.ForeignKey(Mid_Topic,null=True,on_delete=models.SET_NULL,related_name="Mid_subtopics03")
    exercisetypy        = models.ForeignKey(Mid_ExersiseType,null=True,on_delete=models.SET_NULL,related_name="Mid_exercisetypys03")
    exercise            = RichTextField(blank=True, null=True)
    is_Done             = models.BooleanField(default=False)
    is_Free             = models.BooleanField(default=True)
    is_True             = models.ForeignKey(Mid_is_True,null=True,on_delete=models.SET_NULL,related_name="Mid_istrues03")
    A                   = models.CharField(max_length=190,null=True,blank=True)
    B                   = models.CharField(max_length=190,null=True,blank=True)
    C                   = models.CharField(max_length=190,null=True,blank=True)
    D                   = models.CharField(max_length=190,null=True,blank=True)
    A_Image             = models.FileField(default="/" , upload_to='static',null=True,blank=True)
    alternative_A_Image = models.CharField(max_length=190,null=True,blank=True,default='image')
    B_Image             = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    alternative_B_Image = models.CharField(max_length=190,null=True,blank=True,default='image')
    C_Image             = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    alternative_C_Image = models.CharField(max_length=190,null=True,blank=True,default='image')
    D_Image             = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    alternative_D_Image = models.CharField(max_length=190,null=True,blank=True,default='image')
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    File                = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    image               = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    alternative_image   = models.CharField(max_length=190,null=True,blank=True)
    explanation         = models.CharField(max_length=190,null=True,blank=True)
    def __str__(self):
        return self.exercise

# 040_Table Mid_Link_Exercises
class Mid_Link_Exercises(models.Model):
    user          = models.CharField(max_length=190,null=True)
    exercise      = models.CharField(max_length=190,null=True)
    duration_Time = models.TimeField()
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.exercise

# 041_Table Mid_certificate
class Mid_Certificate(models.Model):
    Certificate_Title   = models.CharField(max_length=190,null=True)
    Certificate         = models.TextField(max_length=2500,null=True)
    topic               = models.ForeignKey(Mid_Topic,null=True,on_delete=models.SET_NULL,related_name="Mid_prtopic")
    unit                = models.ForeignKey(Mid_Uint,null=True,on_delete=models.SET_NULL,related_name="Mid_prunit")
    image               = models.FileField(upload_to='static',null=True,blank=True)
    alternative_image   = models.CharField(max_length=190,null=True,blank=True,default='image')
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Certificate_Title

# 042_Table Mid_Link_certificate
class Mid_Link_Certificate(models.Model):
    user               = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="Mid_prUsers")
    certificate        = models.ForeignKey(Mid_Certificate,null=True,on_delete=models.SET_NULL,related_name="Mid_prcertificate")
    topic              = models.ForeignKey(Mid_Topic,null=True,on_delete=models.SET_NULL,related_name="Mid_prtopic1")
    unit               = models.ForeignKey(Mid_Uint,null=True,on_delete=models.SET_NULL,related_name="Mid_prunit1")
    duration_Time      = models.TimeField()
    image              = models.FileField(upload_to='static',null=True,blank=True)
    lternative_image   = models.CharField(max_length=190,null=True,default='image')
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at         = models.DateTimeField(auto_now=True)
    duration_Time      = models.TimeField()

# Mutual_Table
# 043_Table Procedure
class Procedure(models.Model):
    PROCEDURES=(
        ('Assignment','Assignment'),
        ('Exam','Exam'),
        ('Class','Class'),
    )
    Procedure         = models.CharField(unique=True,max_length=190,null=True,choices=PROCEDURES)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Procedure

# 043_Table TopicType
class TopicType(models.Model):
    TOPICTYPE=(
        ('EASY','EASY'),
        ('MEDIUM','MEDIUM'),
        ('HARD','HARD'),
    )
    TopicType         = models.CharField(unique=True,max_length=190,null=True,choices=TOPICTYPE)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.TopicType

# 043_Table DurationTime
class DurationTime(models.Model):
    DURATIONTIME=(
        ('00:15','00:15'),
        ('00:30','00:30'),
        ('00:45','00:45'),
        ('01:00','01:00'),
    )
    Duration         = models.CharField(unique=True,max_length=190,null=True,choices=DURATIONTIME)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Duration

# 044_Table Schoole
class Schoole(models.Model):
    name          = models.CharField(max_length=190,null=True)
    email         = models.CharField(max_length=190,null=True)
    address       = models.CharField(max_length=190,null=True)
    mobile        = models.CharField(max_length=190,null=True)
    rate          = models.CharField(max_length=190,null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

# 045_Table Student
class Student(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# 046_Table Section
class Section(models.Model):
    title         = models.CharField(unique=True,max_length=190,null=True)
    section       = models.CharField(unique=True,max_length=190,null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

# 047_Table StudentSchoole
class StudentSchoole(models.Model):
    student       = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL,related_name="student04")
    schoole       = models.ForeignKey(Schoole,null=True,blank=True,on_delete=models.SET_NULL,related_name="schoole04")
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

# 048_Table StudentClass
class StudentClass(models.Model):
    student         = models.ForeignKey(User,unique=True,null=True,blank=True,on_delete=models.SET_NULL,related_name="student03")
    level           = models.ForeignKey(Level,null=True,blank=True,on_delete=models.SET_NULL,related_name="level03")
    kgclass         = models.ForeignKey(Classes,null=True,blank=True,on_delete=models.SET_NULL,related_name="Classes03")
    prclass         = models.ForeignKey(Pr_Classes,null=True,blank=True,on_delete=models.SET_NULL,related_name="Classes04")
    midclass        = models.ForeignKey(Mid_Classes,null=True,blank=True,on_delete=models.SET_NULL,related_name="Classes05")

# 049_Table StudentClass
class StudentSection(models.Model):
    student       = models.ForeignKey(User,unique=True,null=True,blank=True,on_delete=models.SET_NULL,related_name="student05")
    section       = models.ForeignKey(Section,null=True,blank=True,on_delete=models.SET_NULL,related_name="Section03")
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    
# 050_Table StudentClass
class StudentSubject(models.Model):
    student         = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL,related_name="student06")
    level           = models.ForeignKey(Level,null=True,blank=True,on_delete=models.SET_NULL,related_name="level06")
    kgsubject       = models.ForeignKey(Kin_CategoriesClass,null=True,blank=True,on_delete=models.SET_NULL,related_name="subject03")
    prsubject       = models.ForeignKey(Pr_Subject,null=True,blank=True,on_delete=models.SET_NULL,related_name="subject04")
    midsubject      = models.ForeignKey(Mid_Subject,null=True,blank=True,on_delete=models.SET_NULL,related_name="subject05")

# 051_Table StudentAssignment
class StudentAssignment(models.Model):
    student         = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL,related_name="student07")
    level           = models.ForeignKey(Level,null=True,blank=True,on_delete=models.SET_NULL,related_name="level07")
    kgclass         = models.ForeignKey(Classes,null=True,blank=True,on_delete=models.SET_NULL,related_name="Classes07")
    prclass         = models.ForeignKey(Pr_Classes,null=True,blank=True,on_delete=models.SET_NULL,related_name="Classes08")
    midclass        = models.ForeignKey(Mid_Classes,null=True,blank=True,on_delete=models.SET_NULL,related_name="Classes09")
    kgsubject       = models.ForeignKey(Kin_CategoriesClass,null=True,blank=True,on_delete=models.SET_NULL,related_name="subject07")
    prsubject       = models.ForeignKey(Pr_Subject,null=True,blank=True,on_delete=models.SET_NULL,related_name="subject08")
    midsubject      = models.ForeignKey(Mid_Subject,null=True,blank=True,on_delete=models.SET_NULL,related_name="subject09")
    kguint          = models.ForeignKey(Topic,null=True,blank=True,on_delete=models.SET_NULL,related_name="Unit01")
    pruint          = models.ForeignKey(Pr_Uint,null=True,blank=True,on_delete=models.SET_NULL,related_name="Unit02")
    mduint          = models.ForeignKey(Mid_Uint,null=True,blank=True,on_delete=models.SET_NULL,related_name="Unit03")
    AssignmentType  = models.ForeignKey(Procedure,null=True,blank=True,on_delete=models.SET_NULL,related_name="Type01")
    kgtopic         = models.ForeignKey(Sub_Topic,null=True,blank=True,on_delete=models.SET_NULL,related_name="Topic01")
    prtopic         = models.ForeignKey(Pr_Topic,null=True,blank=True,on_delete=models.SET_NULL,related_name="Topic02")
    mdtopic         = models.ForeignKey(Mid_Topic,null=True,blank=True,on_delete=models.SET_NULL,related_name="Topic03")
    TopicType       = models.ForeignKey(TopicType,null=True,on_delete=models.SET_NULL,related_name="TypeTopic01")
    Section         = models.ForeignKey(Section,null=True,on_delete=models.SET_NULL,related_name="Section07")
    DurationTime    = models.ForeignKey(DurationTime,null=True,on_delete=models.SET_NULL,related_name="DurationTime07")
    submissionDate  = models.DateTimeField(null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

# 052_Table Post
class Post(models.Model):
    title         = models.CharField(max_length=190,null=True)
    post          = models.CharField(max_length=500,null=True)
    user          = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="User05")
    image         = models.FileField(default="/" ,upload_to='static',null=True,blank=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

# 053_Table Like
class Like(models.Model):
    Like          = models.BooleanField(default=False)
    post          = models.ForeignKey(Post,null=True,on_delete=models.SET_NULL,related_name="Post06")
    user          = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="User06")
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

# 054_Table Comment
class Comment(models.Model):
    Comment       = models.CharField(max_length=190,null=True)
    post          = models.ForeignKey(Post,null=True,on_delete=models.SET_NULL,related_name="Post07")
    user          = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="User07")
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Comment

# 055_Table Parent
class Parent(models.Model):
    Parent_ID     = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="User11")
    Student_ID    = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="User12")



User = get_user_model()

def deserialize_user(user):
    return {
        'id': user.id, 'username': user.username, 'email': user.email,
        'first_name': user.first_name, 'last_name': user.last_name
    }

class TrackableDateModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def _generate_unique_uri():
    return str(uuid4()).replace('-', '')[:15]


class ChatSession(TrackableDateModel):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    uri = models.URLField(default=_generate_unique_uri)


class ChatSessionMessage(TrackableDateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    chat_session = models.ForeignKey(
        ChatSession, related_name='messages', on_delete=models.PROTECT
    )
    message = models.TextField(max_length=2000)

    def to_json(self):
        return {'user': deserialize_user(self.user), 'message': self.message}


class ChatSessionMember(TrackableDateModel):
    chat_session = models.ForeignKey(
        ChatSession, related_name='members', on_delete=models.PROTECT
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)
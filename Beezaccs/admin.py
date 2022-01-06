from django.contrib import admin
from .models import Categories , Exercises , ContactUs , Kin_CategoryType , CategoriesOffline , Kin_CategoriesClass , Level , Classes , Kin_ExercisesOnline , ExersiseType , Kin_ExercisesOffline , Topic , is_True , Sub_Topic , Link_Topic , Link_Sub_Topic
from .models import Pr_Classes , Pr_Subject  , Pr_ExercisesOnline , Pr_Link_Topic , Pr_Link_Sub_Topic , Pr_Summary , Pr_ExersiseType , Pr_is_True  , Pr_Uint , Pr_Link_Exercises , Pr_Certificate , Pr_Link_Certificate , Pr_Topic
from .models import Mid_Classes , Mid_Subject  , Mid_ExercisesOnline , Mid_Link_Topic , Mid_Link_Sub_Topic , Mid_Summary , Mid_ExersiseType , Mid_is_True  , Mid_Uint , Mid_Topic , Mid_Link_Exercises , Mid_Certificate , Mid_Link_Certificate
from .models import Procedure , TopicType , DurationTime , Schoole , Student , Section , StudentSchoole , StudentClass , StudentSection , StudentSubject , StudentAssignment , Post , Like , Comment
from accounts.models import User
# Register your models here.
# PHASE01
admin.site.register(Categories)
admin.site.register(Exercises)
admin.site.register(User)
admin.site.register(ContactUs)
admin.site.register(Kin_CategoryType)
admin.site.register(CategoriesOffline)
admin.site.register(Kin_CategoriesClass)
admin.site.register(Level)
admin.site.register(Classes)
admin.site.register(Kin_ExercisesOffline)
admin.site.register(ExersiseType)
# admin.site.register(Kin_ExercisesOnline)
admin.site.register(Topic)
admin.site.register(is_True)
admin.site.register(Sub_Topic)
admin.site.register(Link_Topic)
admin.site.register(Link_Sub_Topic)
# Register your models here.
# PHASE02
admin.site.register(Pr_Classes)
admin.site.register(Pr_Subject)
admin.site.register(Pr_Link_Topic)
admin.site.register(Pr_Link_Sub_Topic)
admin.site.register(Pr_Summary)
admin.site.register(Pr_ExersiseType)
admin.site.register(Pr_is_True)
admin.site.register(Pr_Uint)
# admin.site.register(Pr_ExercisesOnline)
admin.site.register(Pr_Link_Exercises)
admin.site.register(Pr_Certificate)
admin.site.register(Pr_Link_Certificate)
admin.site.register(Pr_Topic)
# PHASE02
admin.site.register(Mid_Classes)
admin.site.register(Mid_Subject)
admin.site.register(Mid_Link_Topic)
admin.site.register(Mid_Link_Sub_Topic)
admin.site.register(Mid_Summary)
admin.site.register(Mid_ExersiseType)
admin.site.register(Mid_is_True)
admin.site.register(Mid_Uint)
admin.site.register(Mid_Topic)
admin.site.register(Mid_ExercisesOnline)
admin.site.register(Mid_Link_Exercises)
admin.site.register(Mid_Certificate)
admin.site.register(Mid_Link_Certificate)
# To All API
admin.site.register(Procedure)
admin.site.register(TopicType)
admin.site.register(DurationTime)
admin.site.register(Schoole)
admin.site.register(Student)
admin.site.register(Section)
admin.site.register(StudentSchoole)
admin.site.register(StudentClass)
admin.site.register(StudentSection)
admin.site.register(StudentSubject)
admin.site.register(StudentAssignment)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)


class Kin_ExercisesAdmin(admin.ModelAdmin):
    list_display = ['classes' , 'categories' , 'topic' , 'sub_topic' , 'exercise']
    search_fields = ['exercise']
admin.site.register(Kin_ExercisesOnline, Kin_ExercisesAdmin)


class PR_ExercisesAdmin(admin.ModelAdmin):
    list_display = ['classes' , 'subject' , 'unit' , 'topic' , 'exercise']
    search_fields = ['exercise']
admin.site.register(Pr_ExercisesOnline, PR_ExercisesAdmin)
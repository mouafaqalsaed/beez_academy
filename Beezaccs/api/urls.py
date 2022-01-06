from django.urls import  path
from rsa import PrivateKey
    # Import PHASE01
from Beezaccs.api.views import ExercisesListCreateAPIView , ExercisesDetailUpdateAndDeletedAPIView , CategoriesListCraeteAPIView , CategoriesDetailAPIView , ContactUsCreate , CategoryTypeAPIView , PrivateMDashborad
    # PHASE02
    # PHASE02-->Kindergarten
from Beezaccs.api.views import LevelsAPIView , GetCategoriesToKgLevel , kgClasses , kgsubjects , ExercisesTopic , ExercisesSubTopic , ExercisesTopicSubTopic , ExercisesAPIView , AnswerExercisesAPIView , AnswerExerciseAPIView , ResultAnswerAPIView , InsertExerciseAPIView , ExerciseAPIView
    # PHASE02
    # PHASE02-->Primary
from Beezaccs.api.views import prClasses , prSubjects , prUints , prTopics , prSummary , prExercises , prExercise , prAnswerExercises , prAnswerExercise , prResultAnswer , prInsertExercise , prUnitsTopics
    # PHASE02
    # PHASE02-->social Media
from Beezaccs.api.views import UserDetails , ActiveTasks , Posts , LikePost , CommentPost , StClassSubject , AnswerQuestions , CorrectAnswer , InCorrectAnswer , ThClassSubject , ThProcedure , ThClass , ThSubject , ThUnit , ThTopic , ThQuestionType , ThCorrectAnswer , ThInsertQuestion , ThTypeTopic , ThDurationTime , ThInsertAssignment , ThSection , ThInsertSection , ThSearchStudent , ThStudentClass , ThInsertStudentSection , ThTotalStudent , ThTotalAssignmentStudent , ThTotalExamStudent , ThAllStudent , ThCountExersisesStudent , ThCreatePost , StCreatePost , PrChildrenID , PrInsertAssignment , ThDeleteStudentSection
    # Service Message
# from Beezaccs.api.views import CreateChatSessionView , UserChatSessionView , MessageGetChatView , MessagePostChatView
urlpatterns = [
    # PHASE01
    path ("Exercises/" , ExercisesListCreateAPIView.as_view() , name="Exercises"),
    path ("Exercises/<int:pk>/" , ExercisesDetailUpdateAndDeletedAPIView.as_view() , name="Exercises-Detail"),
    path ("categories/" , CategoriesListCraeteAPIView.as_view() , name="Categories"),
    path ("categories/<int:pk>/" , CategoriesDetailAPIView.as_view() , name="Categories-Detail"),
    path ("countactUs-create/" , ContactUsCreate.as_view() , name="CountactUs-Create" ),
    path ("CategoryType/" , CategoryTypeAPIView.as_view() , name="CategoryType" ),
    # PHASE02
    # To Return Dashborad To Mr.Mohamed.
    path ("pv-mah/" , PrivateMDashborad.as_view() , name="Dashborad-Detail"),
    # PHASE02-->Kindergarten
    # To Return All Level.
    path ("all-levels/" , LevelsAPIView.as_view() , name="Levels"),
    # To Return Type Level Kindergarten.
    path ("kg-type/" , GetCategoriesToKgLevel.as_view() , name="Levels-Detail"),
    # To Return Classes Level Kindergarten.
    path ("kg-classes/" , kgClasses.as_view() , name="Classes-Detail"),
    # To Return subjects To Specific Class Level Kindergarten.
    path ("kg-subjects/" , kgsubjects.as_view() , name="Categories-Detail"),
    # To Return Topics To Specific Class And Specific Category Level Kindergarten.
    path ("kg-units/<ClassName>/<SubjectName>/" , ExercisesTopic.as_view(), name="Topic-Exercises-Online"),
    # To Return SubTopic To Specific Topics Level Kindergarten.
    path ("kg-topics/<TobicName>/" , ExercisesSubTopic.as_view(), name="SubTopic-Exercises-Online"),
    # To Return Topics And SubTopics To Specific Class And Specific Category Level Kindergarten.
    path ("kg-unitsTopics/<ClassName>/<SubjectName>/" , ExercisesTopicSubTopic.as_view() , name="Topic-SubTopic-Exercises-Online"),
    # To Return All Exercises To Specific Class And Specific Category And Specific Topic And Specific SubTopics Level Kindergarten.
    path ("kg-exercises/<ClassName>/<SubjectName>/<TopicName>/<SubTopicName>/" , ExercisesAPIView.as_view() , name="Exercises-Online"),
    # To Return All Answer Exercises To Specific Class And Specific Category And Specific Topic And Specific SubTopics Level Kindergarten.
    path ("kg-AnswerExercises/<ClassName>/<SubjectName>/<TopicName>/<SubTopicName>/" , AnswerExercisesAPIView.as_view() , name="Answer-Exercises-Online"),
    #To Return Specific Exercise Level Kindergarten.
    path ("kg-exercise/<ID>/" , ExerciseAPIView.as_view() , name="Exercise-Online"),
    # To Return Answer To Specific Exercises Level Kindergarten.
    path ("kg-answer/<ID>/" , AnswerExerciseAPIView.as_view() , name="Exercise-Answer"),
    # To Return Result About Answer User
    path ("kg-result/<ID>/<Answer>/" , ResultAnswerAPIView.as_view() , name="Result-Answer"),
    # To Save Answer User
    path ("kg-InsertExercise/<ID_user>/<ID_exercise>/<Time>/<Answer>/<TrueAnswer>/" , InsertExerciseAPIView.as_view() , name="Insert-Exercise"),
    # PHASE02
    # PHASE02-->Primary
    # To Return Classes Level Primary.
    path ("pr-classes/" , prClasses.as_view() , name="Classes-Detail"),
    # To Return subjects To Specific Class Level Primary.
    path ("pr-subjects/<ClassName>/" , prSubjects.as_view() , name="Subjects-Detail"),
    # To Return Uint To Specific Class And Specific subject Level Primary.
    path ("pr-uints/<ClassName>/<SubjectName>/" , prUints.as_view(), name="Uint-Detail"),
    # To Return Topic To Specific Uint Level Primary.
    path ("pr-topic/<UnitName>/" , prTopics.as_view(), name="Topic-Detail"),
    # To Return Units And Topics To Specific Class And Specific Subject Level Primary.
    path ("pr-unitsTopics/<ClassName>/<SubjectName>/" , prUnitsTopics.as_view() , name="Units-Topic-Exercises-Online"),
    # To Return Summary To Specific Class And Specific subject Level Primary.
    path ("pr-summary/<TobicName>/" , prSummary.as_view(), name="Summary-Detail"),
    # To Return All Exercises To Specific Class And Specific Subject And Specific Topic And Specific Unit Level Primary.
    path ("pr-exercises/<ClassName>/<SubjectName>/<UnitName>/<TopicName>/" , prExercises.as_view() , name="Exercises-Online"),
    #To Return Specific Exercise Level Primary.
    path ("pr-exercise/<ID>/" , prExercise.as_view() , name="Single-Exercise-Online"),
    # To Return All Answer Exercises To Specific Class And Specific Category And Specific Topic And Specific SubTopics Level Primary.
    path ("pr-answerExercises/<ClassName>/<SubjectName>/<UnitName>/<TopicName>/" , prAnswerExercises.as_view() , name="Answer-Exercises-Online"),
    # To Return Answer To Specific Exercises Level Primary.
    path ("pr-answer/<ID>/" , prAnswerExercise.as_view() , name="Exercise-Answer"),
    # To Return Result About Answer User
    path ("pr-result/<ID>/<Answer>/" , prResultAnswer.as_view() , name="Result-Answer"),
    # To Save Answer User   
    path ("pr-InsertExercise/<ID_user>/<ID_exercise>/<Time>/<Answer>/<TrueAnswer>/" , prInsertExercise.as_view() , name="Insert-Exercise"),

    # To Return User Details
    path ("th-user-info/<ID_user>/" , UserDetails.as_view() , name="User-Details"),
    # To Return active tasks Details
    path ("th-active-tasks/<ID_user>/" , ActiveTasks.as_view() , name="Active-Tasks"),
    # To Return Posts Details
    path ("th-posts/<ID_user>/<Par>/" , Posts.as_view() , name="Posts"),
    # To Return Like Of Post
    path ("th-like-post/<ID_post>/" , LikePost.as_view() , name="LikePost"),
    # To Return Comment Of Post
    path ("th-comment-post/<ID_post>/" , CommentPost.as_view() , name="CommentPost"),
    # To Return Class Subject
    path ("st-class-subject/<ID_user>/" , StClassSubject.as_view() , name="ClassSubject"),
    # To Return Answer Questions
    path ("st-answer-questions/<ID_user>/" , AnswerQuestions.as_view() , name="AnswerQuestions"),
    # To Return Correct Answer Questions
    path ("st-correct-answer/<ID_user>/" , CorrectAnswer.as_view() , name="CorrectAnswer"),
    # To Return InCorrect Answer Questions
    path ("st-incorrect-answer/<ID_user>/" , InCorrectAnswer.as_view() , name="InCorrectAnswer"),
    # To Return Class Subject
    path ("th-class-subject/<ID_user>/" , ThClassSubject.as_view() , name="ClassSubject"),
    # To Return Class Subject
    path ("th-procedure/" , ThProcedure.as_view() , name="ThProcedure"),
    # To Return Class
    path ("th-class/<ID_user>/" , ThClass.as_view() , name="ThClass"),
    # To Return Subject about class
    path ("th-subject/<ID_user>/<ID_class>/" , ThSubject.as_view() , name="ThSubject"),
    # To Return Unit about Subject
    path ("th-unit/<ID_user>/<ID_class>/<ID_subject>/" , ThUnit.as_view() , name="ThUnit"),
    # To Return Topic about Unit
    path ("th-topic/<ID_user>/<ID_class>/<ID_subject>/<ID_unit>/" , ThTopic.as_view() , name="ThTopic"),
    # To Return Question Type
    path ("th-question-type/<ID_user>/" , ThQuestionType.as_view() , name="ThQuestionType"),
    # To Return Correct Answer
    path ("th-correct-answer/<ID_user>/" , ThCorrectAnswer.as_view() , name="ThCorrectAnswer"),
    # To Insert Question
    path ("th-insert-question/<ID_user>/<ID_class>/<ID_subject>/<ID_unit>/<ID_topic>/<ID_type>/<question>/<A>/<B>/<C>/<D>/<ID_correct>/<Explanation>/" , ThInsertQuestion.as_view() , name="ThInsertQuestion"),
    # To Type Topic
    path ("th-type-topic/" , ThTypeTopic.as_view() , name="ThTypeTopic"),
    # To Duration Time
    path ("th-duration-time/" , ThDurationTime.as_view() , name="ThDurationTime"),
    # To Insert Assignment
    path ("th-insert-assignment/<ID_user>/<ID_pro_Type>/<ID_class>/<ID_section>/<ID_subject>/<ID_unit>/<ID_topic>/<ID_type>/<submissiondate>/<ID_duration>/" , ThInsertAssignment.as_view() , name="ThInsertAssignment"),
    # To Section Name
    path ("th-section/" , ThSection.as_view() , name="ThSection"),
    # To Insert Section
    path ("th-insert-section/<SectionName>/" , ThInsertSection.as_view() , name="ThInsertSection"),
    # To Search About Student
    path ("th-search-student/<Name>/" , ThSearchStudent.as_view() , name="ThSearchStudent"),
    # To Return Student Class
    path ("th-student-class/<ID_user>/" , ThStudentClass.as_view() , name="ThStudentClass"),
    # To Insert Student Section
    path ("th-insert-student-section/<ID_user>/<ID_class>/<ID_section>/<ID_subject>/<ID_student>/" , ThInsertStudentSection.as_view() , name="ThInsertStudentSection"),
    # To Delete Student Section
    path ("th-delete-student-section/<ID_user>/<ID_class>/<ID_section>/<ID_subject>/<ID_student>/" , ThDeleteStudentSection.as_view() , name="ThDeleteStudentSection"),
    # To Return Total Student
    path ("th-total-student/<ID_user>/<ID_class>/<ID_section>/<ID_subject>/" , ThTotalStudent.as_view() , name="ThTotalStudent"),
    # To Return Exam Student
    path ("th-exam-student/<ID_user>/<ID_class>/<ID_section>/<ID_subject>/" , ThTotalExamStudent.as_view() , name="ThTotalExamStudent"),
    # To Return Assignment Student
    path ("th-assignment-student/<ID_user>/<ID_class>/<ID_section>/<ID_subject>/" , ThTotalAssignmentStudent.as_view() , name="ThTotalAssignmentStudent"),
    # To Return Student
    path ("th-student/<ID_user>/<ID_class>/<ID_section>/<ID_subject>/" , ThAllStudent.as_view() , name="ThAllStudent"),
    # To Return Count Exersise Student
    path ("th-count-exersise-student/<ID_user>/<ID_class>/<ID_subject>/" , ThCountExersisesStudent.as_view() , name="ThCountExersisesStudent"),
    # To Teacher Insert Post
    path ("th-create-post/<ID_user>/<post>/<ImagePost>/" , ThCreatePost.as_view() , name="ThCreatePost"),
    # To Student Insert Post
    path ("st-create-post/<ID_user>/<post>/<ImagePost>/" , StCreatePost.as_view() , name="STCreatePost"),
    # To Return Children Id
    path ("pr-childern-id/<ID_user>/" , PrChildrenID.as_view() , name="PrChildrenID"),
    # To Insert Assignment From Parent
    path ("pr-insert-assignment/<ID_user>/<ID_student>/<ID_pro_Type>/<ID_class>/<ID_section>/<ID_subject>/<ID_unit>/<ID_topic>/<ID_type>/<submissiondate>/<ID_duration>/" , PrInsertAssignment.as_view() , name="ThInsertAssignment"),
    # To Service Mesaage
    # # To Create New Section Chat
    # path ("new-chats/<ID_user>/" , CreateChatSessionView.as_view() , name="NewChat"),
    # # To Create New User In Chat
    # path ("user-chats/<ID_user>/<uri>/" , UserChatSessionView.as_view() , name="NewUserINChat"),
    # # To Get All Message In Chat
    # path ("message-chats/<uri>/" , MessageGetChatView.as_view() , name="GetMessage"),
    # # To Create  Message In Chat
    # path ("message-chats/<ID_user>/<uri>/<message>/" , MessagePostChatView.as_view() , name="PostMessage")
]
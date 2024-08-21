from rest_framework import serializers
from student.models import Student
from classes.models import Class
from classroom_period.models import ClassroomPeriod
from courses.models import Courses
from teacher.models import Teacher
from datetime import date, datetime


  
class TeacherSerializer(serializers.ModelSerializer):
 class Meta:
    model=Teacher
    fields = "__all__"

      
class ClassesSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model=Class
        fields="__all__"
        

class CoursesSerializer(serializers.ModelSerializer):
  teacher = TeacherSerializer()
  class Meta:
    model=Courses
    fields = "__all__"
    
        
class StudentSerializer(serializers.ModelSerializer):
  courses = CoursesSerializer(many=True)
  class Meta:
        model = Student
        fields = "__all__"
    
        
class ClassroomPeriodSerializer(serializers.ModelSerializer):
  student_class = StudentSerializer()
  class Meta:
    model=ClassroomPeriod
    fields="__all__"
    

class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    def get_full_name(self, Student):
        return f"{Student.first_name} {Student.last_name}"
    
    class Meta:
        model = Teacher
        fields = ['id', 'full_name','email']
  
class MinimalCourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Courses
    fields = ['id','name','teacher']
    
class MinimalClassSerializer(serializers.ModelSerializer):
  class Meta:
    model = Class
    field = ['class_id', 'class_name', 'names_of_teachers']
    
class MinimalStudentSerializer(serializers.ModelSerializer):
   full_name = serializers.SerializerMethodField()
   age = serializers.SerializerMethodField()
   
   def get_full_name(self, Student):
     return f"{Student.first_name} {Student.last_name}"
   
   def get_age(self, Student):
     if Student.date_of_birth:
       today = datetime.now()
     if isinstance(Student.date_of_birth, date) and not isinstance(Student.date_of_birth, datetime):
       date_of_birth = datetime.combine(Student.date_of_birth, datetime.min.time())
     else:
       date_of_birth = Student.date_of_birth
       
     age = today - date_of_birth
     return age.days // 365
   
   class Meta:
    model = Student
    fields = ['id','full_name','email','age']
    

class MinimalClassPeriodSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClassroomPeriod
    fields = ['start_time','classroom','end_time']
     
       
    
    


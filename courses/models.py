from django.db import models
from teacher.models import Teacher

# Create your models here.
class Courses(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_name = models.CharField(max_length = 20).primary_key
    course_id = models.SmallIntegerField()
    department = models.CharField(max_length = 20)
    course_discription = models.TextField()
    class_starting_time = models.TimeField(00, 00, 00)
    course_instructor = models.CharField(max_length = 28)
    number_of_students = models.PositiveSmallIntegerField()
    grade_level = models.PositiveSmallIntegerField()
    school_term = models.IntegerField()
    assement_requirements = models.TextField()
    course_trainer_name = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.course_name} {self.course_trainer_name}"
    

    

from django.test import TestCase
from .models import Student
from .forms import StudentRegistrationForm

# Create your tests here.

class StudentTest(TestCase):
    def setUp(self):
       self.student = Student(
            first_name = "Canary",
            last_name = "Mugume",
            email = "priscillamikisa@gmail.com",
            student_code = 112,
            country = "Uganda",
            gender = "female",
            bio = "Still moving.......",
            id_number = 21,
            grade_level = 4,
            gurdian_name = "Dakota",
            student_next_of_kin = "Huffy",
            student_national_id_number = "578h0h32808bs",
       )
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name, self.student.full_name())
        
    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name, self.student.full_name())
        
    
class StudentFormTest(TestCase):
        def test_student_form_validity(self):
            form_data = {
                "first_name": "Canary",
                "last_name": "Mugume",
                "email": "priscillamikisa@gmail.com",
                "student_code": 112,
                "country": "Uganda",
                "gender": "female",
                "bio": "Still moving.......",
                "id_number": 21,
                "grade_level":4,
                "gurdian_name":"Dakota",
                "student_next_of_kin":"Huffy",
                "student_national_id_number":"578h0h32808bs",
            }
            
            form = StudentRegistrationForm(data=form_data)
            self.assertTrue(form.is_valid())

            
        
        
        def test_student_form_invalid(self):
            form_data={"first_name":"Mikisa", "last_name":"Priscilla"}
            form = StudentRegistrationForm(data=form_data)
            self.assertFalse(form.is_valid())
            self.assertIn('email', form.errors)
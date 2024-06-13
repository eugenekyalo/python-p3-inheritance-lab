# lib/testing/user_test.py
import unittest
from lib.user import User
from lib.teacher import Teacher
from lib.student import Student

class TestUser(unittest.TestCase):
    def test_user_initialization(self):
        user = User("Jane", "Doe")
        self.assertEqual(user.first_name, "Jane")
        self.assertEqual(user.last_name, "Doe")

class TestTeacher(unittest.TestCase):
    def test_teacher_inherits_user(self):
        teacher = Teacher("John", "Doe")
        self.assertEqual(teacher.first_name, "John")
        self.assertEqual(teacher.last_name, "Doe")

    def test_teacher_knowledge(self):
        teacher = Teacher("John", "Doe")
        self.assertIn(teacher.teach(), teacher.knowledge)

class TestStudent(unittest.TestCase):
    def test_student_inherits_user(self):
        student = Student("Jane", "Doe")
        self.assertEqual(student.first_name, "Jane")
        self.assertEqual(student.last_name, "Doe")

    def test_student_learn(self):
        student = Student("Jane", "Doe")
        student.learn("Python OOP")
        self.assertIn("Python OOP", student.knowledge)

if __name__ == '__main__':
    unittest.main()

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from datetime import date, timedelta
from collections import OrderedDict


from .models import Student, User, Teacher, Class, Classroom, Stream


class TeacherAccountCreattionTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test2021',is_teacher=True,
                                                         password='12test12',
                                                         email='test2021@example1.com', first_name="test", last_name="test")
        self.user.save()

        #test stream
        self.stream = Stream.objects.create(name ="Economics1")
        self.stream.save()
        #save the users

        self.teacher = Teacher.objects.create(
            user=self.user,
            stream = self.stream
            )
        self.teacher.save()

    def tearDown(self):
        self.teacher.delete()
        self.stream.delete()
        self.user.delete()


    def testCorrectDetails(self):
        user = authenticate(username='test2021', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def testWrongUsername(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def testWrongPassword(self):
        user = authenticate(username='test2021', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)



class TeacherORStudentTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test2022',is_teacher=True,
                                                         password='12test12',
                                                         email='test2022@example1.com', first_name="test", last_name="test")
        self.user.save()

        #test stream
        self.stream = Stream.objects.create(name ="Economics1")
        self.stream.save()
        #save the users

        self.teacher = Teacher.objects.create(
            user=self.user,
            stream = self.stream
            )
        self.teacher.save()

    def tearDown(self):
        self.teacher.delete()
        self.stream.delete()
        self.user.delete()


    def testCorrectDetails(self):
        user = authenticate(username='test2022', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)


    def TestStudents(self):
        user = authenticate(username='test2022', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated and not user.is_student)

    def TestTeacher(self):
        user = authenticate(username='test2022', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated and user.is_teacher)


#
# class LoginTest(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='test2022',is_teacher=True,
#                                                          password='12test12',
#                                                          email='test2022@example1.com', first_name="test", last_name="test")
#         self.user.save()
#
#         #test stream
#         self.stream = Stream.objects.create(name ="Economics1")
#         self.stream.save()
#         #save the users
#
#         self.teacher = Teacher.objects.create(
#             user=self.user,
#             stream = self.stream
#             )
#         self.teacher.save()
#
#
#     def tearDown(self):
#         self.stream.delete()
#         self.teacher.delete()
#         self.user.delete()
#
#     def testCorrectDetails(self):
#         response = self.client.post('/login/', {'username': 'test', 'password': '12test12'})
#         self.assertTrue(response.request)
#
#     def testWrongUsername(self):
#         response = self.client.post('/login/', {'username': 'wrong', 'password': '12test12'})
#         self.assertFalse(response.request)
#
#     def testWrongPassword(self):
#         response = self.client.post('/login/', {'username': 'test', 'password': 'wrong'})
#         self.assertFalse(response.request)

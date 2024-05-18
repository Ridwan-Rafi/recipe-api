from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test create a new user with ans email is successful"""
        email = 'red@gmail.com'
        password = 'testpass124'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_valid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test1234")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        Email = "superuser@gmail.com"
        Password = "123@asd"
        user = get_user_model().objects.create_superuser(
            email=Email,
            password=Password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

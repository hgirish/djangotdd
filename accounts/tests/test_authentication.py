from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.authentication import PasswordlessAuthenticationBackend
from accounts.models import Token

User = get_user_model()
dummy_email = 'edith@example.com'
class AuthenticateTest(TestCase):
    def test_returns_None_if_no_such_token(self):
        result = PasswordlessAuthenticationBackend().authenticate(
            'no-such-token'
        )
        self.assertIsNone(result)
    def test_returns_new_user_with_correct_email_if_token_exists(self):
        token = Token.objects.create(email=dummy_email)
        user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        new_user = User.objects.get(email=dummy_email)
        self.assertEqual(user,new_user)
    def test_returns_existing_user_with_correct_email_if_token_exists(self):
        existing_user = User.objects.create(email=dummy_email)
        token = Token.objects.create(email=dummy_email)
        user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        self.assertEqual(user, existing_user)
class GetUserTest(TestCase):
    def test_gets_user_by_email(self):
        User.objects.create(email='another@example.com')
        desired_user= User.objects.create(email=dummy_email)
        found_user = PasswordlessAuthenticationBackend().get_user(dummy_email)
        self.assertEqual(found_user,desired_user)
    def test_returns_None_if_no_user_with_email(self):
        self.assertIsNone(
            PasswordlessAuthenticationBackend().get_user(dummy_email)
        )

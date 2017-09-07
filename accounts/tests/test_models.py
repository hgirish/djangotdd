from django.test import TestCase
from django.contrib import auth
from accounts.models import Token 

# Create your tests here.
User = auth.get_user_model()
dummyemail = 'a@b.com'
class UserModelTest(TestCase):
    
    def test_user_is_valid_with_email_only(self):
        user = User(email=dummyemail)
        user.full_clean() # Should not raise
    def test_email_is_primary_key(self):
        user=User(email=dummyemail)
        self.assertEqual(user.pk, dummyemail)
    def test_no_problem_with_auth_login(self):
        user = User.objects.create(email=dummyemail)
        user.backend = ''
        request = self.client.request().wsgi_request 
        auth.login(request,user) # should not raise 
class TokenModelTest(TestCase):
    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email=dummyemail)
        token2 = Token.objects.create(email=dummyemail)
        self.assertNotEqual(token1.uid, token2.uid)
        

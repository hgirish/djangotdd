from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Token 

# Create your tests here.
User = get_user_model()
dummyemail = 'a@b.com'
class UserModelTest(TestCase):
    
    def test_user_is_valid_with_email_only(self):
        user = User(email=dummyemail)
        user.full_clean() # Should not raise
    def test_email_is_primary_key(self):
        user=User(email=dummyemail)
        self.assertEqual(user.pk, dummyemail)
class TokenModelTest(TestCase):
    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email=dummyemail)
        token2 = Token.objects.create(email=dummyemail)
        self.assertNotEqual(token1.uid, token2.uid)
        

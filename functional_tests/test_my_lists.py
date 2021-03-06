from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
from django.contrib.sessions.backends.db import SessionStore
from .base import FunctionalTest
#from superlists.settings.base import AUTHENTICATION_BACKENDS
User = get_user_model()
dummy_email = 'edith@example.com'


class MyListTest(FunctionalTest):
    def create_pre_authenticated_session(self, email):
        user = User.objects.create(email=email)
        session = SessionStore()
        session[SESSION_KEY] = user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.save()

        # to set a cookie we need to visit the domain
        # 404 pages loads the quickest
        self.browser.get(self.live_server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key,
            path='/',
        ))

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_out(dummy_email)

        # Edith is a logged in user
        self.create_pre_authenticated_session(dummy_email)
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_in(dummy_email)

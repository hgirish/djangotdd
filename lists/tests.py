from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_home_page_template(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')

        self.assertTemplateUsed(response, 'home.html')

from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_home_page_template(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')

        self.assertTemplateUsed(response, 'home.html')
    def test_can_save_a_POST_request(self):
        response=self.client.post('/', data={'item_text':'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

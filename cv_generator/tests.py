from django.test import TestCase
from django.urls import reverse

class test_Signup(TestCase):
    def test_user_post(self):
        response = self.client.post(reverse('signup'),data={'first_name':'harsh','last_name':'kalal', 'email':'harshkalal2125@gmail.com','username':'Harsh1997','password1':'Hsbfk@1997','password2':'Hsbfk@1997'})
        self.assertEqual(response.status_code, 302)







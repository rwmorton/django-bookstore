from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from accounts.forms import CustomUserCreationForm
from accounts.views import SignupPageView

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='bob',
            email='bob@bob.com',
            password='password!'
        )
        self.assertEqual(user.username,'bob')
        self.assertEqual(user.email,'bob@bob.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='adminPassword!'
        )
        self.assertEqual(user.username,'admin')
        self.assertEqual(user.email,'admin@admin.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'account/signup.html')
        self.assertContains(self.response,'Sign up')
        self.assertNotContains(self.response,'Hi there! I should be on the page!')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username,self.email)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,self.username)
        self.assertEqual(get_user_model().objects.all()[0].email,self.email)

from django.contrib.auth import get_user_model
from django.test import TestCase

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

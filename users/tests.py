from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='teste1',
            email='teste1@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'teste1')
        self.assertEqual(user.email, 'teste1@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    
    def teste_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superteste1',
            email='superteste1@email.com',
            password='testepass123'
        )
        self.assertEqual(admin_user.username, 'superteste1')
        self.assertEqual(admin_user.email, 'superteste1@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

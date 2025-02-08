from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User

class AuthenticationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.token_url = reverse('token_obtain_pair')

    def test_user_can_login(self):
        """
        Teste de login do usuário
        """
        data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_cannot_login_with_wrong_credentials(self):
        """
        Teste de login com credenciais incorretas
        """
        data = {
            'username': 'testuser',
            'password': 'wrongpass'
        }
        
        response = self.client.post(self.token_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
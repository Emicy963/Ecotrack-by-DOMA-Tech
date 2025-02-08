from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.users.models import User
from .models import SustainableAction

class SustainableActionTests(APITestCase):
    def setUp(self):
        # Criar usuário para testes
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Autenticar o usuário
        self.client.force_authenticate(user=self.user)
        
        # Criar uma ação sustentável para testes
        self.action = SustainableAction.objects.create(
            title='Test Action',
            description='Test Description',
            category='WATER',
            points=10,
            user=self.user
        )
        
        # URL para as ações
        self.url = reverse('action-list')

    def test_create_action(self):
        """
        Teste de criação de uma nova ação sustentável
        """
        data = {
            'title': 'New Action',
            'description': 'New Description',
            'category': 'RECYCLING',
            'points': 5
        }
        
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SustainableAction.objects.count(), 2)
        self.assertEqual(self.user.points, 15)  # 10 pontos iniciais + 5 novos

    def test_list_actions(self):
        """
        Teste de listagem das ações sustentáveis
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_action(self):
        """
        Teste de atualização de uma ação sustentável
        """
        url = reverse('action-detail', args=[self.action.id])
        data = {
            'title': 'Updated Action',
            'description': 'Updated Description',
            'category': 'WATER',
            'points': 15
        }
        
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SustainableAction.objects.get().title, 'Updated Action')

    def test_delete_action(self):
        """
        Teste de exclusão de uma ação sustentável
        """
        url = reverse('action-detail', args=[self.action.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SustainableAction.objects.count(), 0)

# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from kennels.models import Kennel
from rest_framework_jwt.settings import api_settings
payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class KennelAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testuser', email='test@test.com')
        user.set_password('randompassword')
        user.save()
        kennel = Kennel.objects.create(owner=user, title='test 1', slug='test_1', type='dogs')
        kennel.save()

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_kennel(self):
        kennel_count = Kennel.objects.count()
        self.assertEqual(kennel_count, 1)

    def test_get_list(self):
        data = {}
        url = api_reverse('kennels:kennel_list')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_list(self):
        data = {'title': 'Test 2', 'type': 'cats'}
        url = api_reverse('kennels:kennel_list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        kennel = Kennel.objects.first()
        data = {}
        url = kennel.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        kennel = Kennel.objects.first()
        data = {'title': 'test 2_2'}
        url = kennel.get_api_url()

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_item_with_user(self):
        kennel = Kennel.objects.first()
        data = {'title': 'test 2_2'}
        url = kennel.get_api_url()

        user = User.objects.first()
        payload = payload_handler(user)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp) # JWT <token>

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_list_with_user(self):
        data = {'title': 'Test 2', 'type': 'cats'}
        url = api_reverse('kennels:kennel_list')

        user = User.objects.first()
        payload = payload_handler(user)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)  # JWT <token>

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_ownership(self):

        owner = User.objects.create(username='testusername2', email='test2@test.com')
        kennel = Kennel.objects.create(owner=owner, title='test 2', slug='test_2', type='cats')
        kennel.save()

        user = User.objects.first()
        self.assertNotEqual(user.username, owner.username)

        payload = payload_handler(user)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)  # JWT <token>

        url = kennel.get_api_url()
        data = {'title': 'test 2_2'}

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # request.post(url, data, headers={"Authorization": "JWT " + <token>})
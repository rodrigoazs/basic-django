from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product
import json


class ProductTests(APITestCase):
    def test_create_product(self):
        """
        Ensure we can create a new product.
        """
        url = reverse('products_list')
        data = {
            'id': 0,
            'title': 'Test title',
            'description': 'Test description',
            'published': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().title, 'Test title')

    def test_get_empty_products_list(self):
        """
        Ensure we can get a empty product list.
        """
        url = reverse('products_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), Product.objects.count())

    def test_get_products_list(self):
        """
        Ensure we can get a product list.
        """
        product = Product(
            title='Beatles Blog',
            description='All the latest Beatles news.',
            published=True
        )
        product.save()
        url = reverse('products_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json.loads(response.content)), Product.objects.count())
        self.assertEqual(json.loads(response.content)[0]['title'], 'Beatles Blog')

    def test_get_product_detail(self):
        """
        Ensure we can get a product detail.
        """
        product = Product(
            id=1,
            title='Beatles Blog',
            description='All the latest Beatles news.',
            published=True
        )
        product.save()
        url = reverse('product_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['title'], 'Beatles Blog')

    def test_update_product_detail(self):
        """
        Ensure we can update a product detail.
        """
        product = Product(
            id=1,
            title='Beatles Blog',
            description='All the latest Beatles news.',
            published=True
        )
        product.save()
        data = {
            'id': 1,
            'title': 'Test title',
            'description': 'Test description',
            'published': True
        }
        url = reverse('product_detail', kwargs={'pk': 1})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['title'], 'Test title')
        self.assertEqual(Product.objects.get(pk=1).title, 'Test title')

    def test_delete_product_detail(self):
        """
        Ensure we can delete a product detail.
        """
        product = Product(
            id=1,
            title='Beatles Blog',
            description='All the latest Beatles news.',
            published=True
        )
        product.save()
        url = reverse('product_detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.item1 = Menu.objects.create(title="Milkshake", price=8, inventory=20)
        self.item2 = Menu.objects.create(title="Soda", price=1, inventory=20)
        self.serializer = MenuItemSerializer(instance=[self.item1,self.item2], many=True)
        
    def test_getall(self):
        response = self.client.get(reverse('menuAPI'))
        self.assertEqual(response.data, self.serializer.data)

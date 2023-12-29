from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.item1 = Menu.objects.create(title="Milkshake", price=8, inventory=20)
        self.item2 = Menu.objects.create(title="Soda", price=1, inventory=20)
        
    def test_getall(self):
        response = self.client.get(reverse('menuAPI'))
        items = Menu.objects.all()
        serializer = MenuItemSerializer(items, many = True)
        self.assertEqual(response.data, serializer.data)
    
    def test_getone(self):
        item = Menu.objects.create(title="Walnut Shrimp", price=22, inventory=25)
        response = self.client.get(f'/restaurant/menu/{item.id}')
        serializer = MenuItemSerializer(item, many = False)
        self.assertEqual(response.data, serializer.data)

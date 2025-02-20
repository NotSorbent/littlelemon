from django.test import TestCase
from django.urls import reverse
from reservation.models import Menu
from reservation.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        """Create test instances of the Menu model."""
        self.item1 = Menu.objects.create(title="Burger", price=10.99, inventory=50)
        self.item2 = Menu.objects.create(title="Pizza", price=15.99, inventory=30)
        self.item3 = Menu.objects.create(title="Pasta", price=12.49, inventory=20)

    def test_getall(self):
        """Retrieve all Menu objects and check if the serialized data matches the response."""
        response = self.client.get(reverse('menu-list'))  # Adjust 'menu-list' if needed

        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)  # Serialize expected data

        self.assertEqual(response.status_code, 200)  # Check response status
        self.assertEqual(response.json()['results'], serializer.data)  # Compare response with expected data
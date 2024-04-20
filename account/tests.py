from django.test import TestCase
from rest_framework.test import APIClient
from .views import Account
from django.urls import reverse

# Create your tests here.
class AccountTestCase(TestCase):
    def setUp(self):
        Account.objects.create(
            client_id = '3h3j4h2ot6t5j342',
            balance = 10000,
            status = 'in_collection',
            consumer_name = 'John Smith',
            address = '123 abc st, Berkeley, CA94700',
            ssn = '384-98-6598',
        )
    
    def test_model_creation(self):
        obj = Account.objects.get(client_id = '3h3j4h2ot6t5j342')
        self.assertEqual(obj.client_id,'3h3j4h2ot6t5j342')



class AccountViewTestCase(TestCase):
    def test_view_creation(self):
        response = self.client.get(reverse('account-list'))
        self.assertEqual(response.status_code, 200)



class AccountViewAPITestCase(TestCase):
    def setUp(self):
        # Create test accounts
        self.account1 = Account.objects.create(
            client_id = "1", 
            balance = 1000.0, 
            status = "ACTIVE", 
            consumer_name = "John Doe",
            address = "123 abc st, Berkeley, CA94700",
            ssn = "384-98-6418",
        )
        self.account2 = Account.objects.create(
            client_id = "2", 
            balance = 500.0, 
            status = "INACTIVE", 
            consumer_name = "Jane Doe",
            address = "123 dfc st, Berkeley, CA94700",
            ssn = "384-71-6598",
        )

    def test_get_queryset(self):
        # Test filtering by min_balance
        url = reverse("account-list") + "?min_balance=600.0"
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["client_id"], self.account1.client_id)

        # Test filtering by max_balance
        url = reverse("account-list") + "?max_balance=600.0"
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["client_id"], self.account2.client_id)

        # Test filtering by status
        url = reverse("account-list") + "?status=active"
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["client_id"], self.account1.client_id)

        # Test filtering by consumer_name
        url = reverse("account-list") + "?consumer_name=john doe"
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["client_id"], self.account1.client_id)
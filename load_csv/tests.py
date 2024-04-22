from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from account.models import Account


class LoadCSVTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        csv_content = (
            "client reference no,balance,status,consumer name,consumer address,ssn\n"
            "12345,1000,ACTIVE,John Doe,123 Main St,123-45-6789\n"
            "67890,500,INACTIVE,Jane Smith,456 Elm St,987-65-4321\n"
        )
        self.csv_file = SimpleUploadedFile(
            "test.csv", csv_content.encode("utf-8"), content_type="text/csv"
        )

    def test_load_csv_success(self):
        url = reverse("load-csv")
        data = {"file": self.csv_file}
        response = self.client.post(url, data, format="multipart")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Account.objects.count(), 2)

    def test_load_csv_no_file_uploaded(self):
        response = self.client.post(reverse("load-csv"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "<h1>No file uploaded or invalid request method</h1>",
            response.content.decode(),
        )

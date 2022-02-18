from django.test import TestCase
from authors.models import Company

# Create your tests here.
class TestModel(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name="Odyssey",
            bio="Tech Company",
            active=True
        )

    def test_valid_company_model(self):
        self.assertEquals(self.company.name, "Odyssey")
        self.assertEquals(self.company.bio, "Tech Company")
        self.assertEquals(self.company.active, True)

    def test_invalid_company_model(self):
        self.assertNotEquals(self.company.name, "Airtel")
        self.assertNotEquals(self.company.bio, "Telecom Company")
        self.assertNotEquals(self.company.active, False)

    def test_count_company_model(self):
        self.count_company = Company.objects.all().count()
        self.assertEquals(self.count_company, 1)

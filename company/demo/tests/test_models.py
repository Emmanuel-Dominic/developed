from django.test import TestCase
from company.demo.models import Company


# Create your tests here.
class TestDemoModels(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
             name='odyssey', location='kagoma',
              vision='software development', logo='null'
            )
        
    def test_company_exists(self):
        self.assertEquals(self.company.name, 'odyssey')
        self.assertEquals(self.company.logo, 'null')
        self.assertEquals(self.company.location, 'kagoma')
        self.assertEquals(self.company.vision, 'software development')
        
    def test_company_doesnot_exists(self):
        self.assertNotEquals(self.company.name, 'google')
        self.assertNotEquals(self.company.logo, 'google.png')
        self.assertNotEquals(self.company.location, 'usa')
        self.assertNotEquals(self.company.vision, 'tech company')
        
    def test_count_company(self):
        self.count = Company.objects.all().count()
        self.assertEquals(self.count, 1)

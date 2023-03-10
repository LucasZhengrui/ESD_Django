from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class Temp_test(TestCase):
    def test_page_load(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200) # 200 means successful, 404 means not found, 502 means bad gateway
        self.assertContains(response, "which spurs him into conflict with")

        # Confirm that the home page loads.
        # Confirm the home page contains the text: "which spurs him into conflict with"

    def test_form_freezing(self):
        client = Client()
        response = client.post('/', {'temp': 32})
        # Confirm that the form works by converting either freezing water temperatures.
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your converted temperature of 32 in F is 0.0 in C")

    def test_form_boiling(self):
        client = Client()
        response = client.post('/', {'temp': 212})
        # Confirm that the form works by converting either boiling water temperatures.
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your converted temperature of 212 in F is 100.008 in C")

    # from .views inport convert
    # def test_temp(self):
    #    self.assertEqual(100.008, convert(212))
    # 
    # Here is another way to test the temp function.

    def test_view_correct_template(self):
        response = self.client.get(reverse('index'))
        # Used 'reverse' from django.urls to test the template of index
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'esd_home/index.html')
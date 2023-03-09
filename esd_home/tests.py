from django.test import TestCase, Client

# Create your tests here.
class Temp_test(TestCase):
    def test_page_load(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
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
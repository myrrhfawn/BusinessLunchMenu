from rest_framework.test import APITestCase

# Create your tests here.

class DailyAPITestCase(APITestCase):
    def test_daily(self):
        url = 'api/v1/daily/'
        response = self.client.get(url)
        print(response)

    def test_menulist(self):
        url = 'api/v1/menulist/'
        response = self.client.get(url)
        print(response)

    def test_requests(self):
        url = 'api/v1/dailyrequest/'
        response = self.client.get(url)
        print(response)

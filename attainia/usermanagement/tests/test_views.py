from rest_framework.test import APIClient, APITestCase
from rest_framework import status
# from .factories import UserActivityFactory


class UserActivityTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        # check for two users - one has logged in, the other has not
        self.has_not_logged_in = {
            'id': '0', 'username': 'ana',
            'last_login': '2019-08-20T22:15:09.926Z',
            'login_count': 0, 'project_count': 12
        }
        self.has_logged_in = {
            'id': '1', 'username': 'tim',
            'last_login': '2019-08-20T22:15:09.926Z',
            'login_count': 23, 'project_count': 234
        }

    def test_get_users_no_filter(self):
        # test call to see all users returned
        response = self.client.get('/users/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.has_not_logged_in, response.data)
        self.assertIn(self.has_logged_in, response.data)

    def test_get_users_filter_logged_in(self):
        response = self.client.get('/users/?loggedin=true')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn(self.has_not_logged_in, response.data)
        self.assertIn(self.has_logged_in, response.data)

    def test_get_users_filter_not_logged_in(self):
        response = self.client.get('/users/?loggedin=false')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.has_not_logged_in, response.data)
        self.assertNotIn(self.has_logged_in, response.data)

    def test_get_users_no_filter_bad_input(self):
        response = self.client.get('/users/?loggedin=234asdf')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.has_not_logged_in, response.data)
        self.assertIn(self.has_logged_in, response.data)


class UserActivityModelTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.base_url = 'http://localhost:8000/'
        # self.user1 = UserActivityFactory()
        # self.user2 = UserActivityFactory()
        # self.user3 = UserActivityFactory()

    # def test_get_users_no_filter(self):
    #     #test call to see all users returned
    #     pass
    #     response = self.client.get(self.base_url + 'activeusers/')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn(self.user1.username, response)
    #
    # def test_get_users_filter_logged_in(self):
    #     response = self.client.get('/activeusers/?loggedin=true')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_get_users_no_filter_not_logged_in(self):
    #     response = self.client.get('/activeusers/?loggedin=false')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    # def test_get_users_no_filter_bad_input(self):
    #     response = self.client.get('/activeusers/?loggedin=234asdf')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

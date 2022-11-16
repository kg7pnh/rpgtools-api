# -*- coding: utf-8 -*-
# TODO: break out into individual files under api/tests/views
"""
Defines test case run against the API for DieRoll model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import ADMIN_USER
from api.tests.base import API_URL
from api.tests.base import CODES
from api.tests.base import RO_USER
from api.tests.base import T_URL

FIXTURES = ['test_users']


@tag("views_admin")
class TestsAdmin(RpgtApiBTC):
    """
    Defines TestAdmin class
    """
    fixtures = FIXTURES
    response = RpgtApiBTC.rpgt_api_cli.post(T_URL,
                                            ADMIN_USER,
                                            format="json").json()
    token = response['access']
    refresh = response['refresh']

    def test_get_current_user(self):
        """
        Submits a POST request
        """
        response = self.rpgt_api_cli.get(API_URL + 'current-user',
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertEqual(response.json()['is_authenticated'], True)
        self.assertEqual(response.json()['username'], 'admin')
        self.assertEqual(response.json()['first_name'], 'admin')
        self.assertEqual(response.json()['last_name'], 'admin')
        self.assertEqual(response.json()['is_superuser'], True)

    def test_get_is_admin(self):
        """
        Submits a POST request
        """
        response = self.rpgt_api_cli.get(API_URL + 'is-admin',
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_token(self):
        """
        Submits a POST request
        """
        response = self.rpgt_api_cli.post(T_URL,
                                          ADMIN_USER,
                                          format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertTrue(response.json()['access'])

    def test_post_token_refresh(self):
        """
        Submits a POST request
        """
        response = self.rpgt_api_cli.post(T_URL + '/refresh',
                                          {"refresh": self.refresh},
                                          format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertTrue(response.json()['access'])

    def test_post_token_verify(self):
        """
        Submits a POST request
        """
        response = self.rpgt_api_cli.post(T_URL + '/refresh/',
                                          {"token": self.token},
                                          format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertFalse(response.json())


@tag("views_readonly")
class TestsReadOnly(RpgtApiBTC):
    """
    Defines TestsReadOnly class
    """
    fixtures = FIXTURES
    response = RpgtApiBTC.rpgt_api_cli.post(T_URL,
                                            RO_USER,
                                            format="json").json()
    token = response['access']
    refresh = response['refresh']

    def test_get_current_user(self):
        """
        Submits a POST request
        """
        response = self.rpgt_api_cli.get(API_URL + 'current-user',
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertEqual(response.json()['is_authenticated'], True)
        self.assertEqual(response.json()['username'], 'read-only')
        self.assertEqual(response.json()['first_name'], 'read')
        self.assertEqual(response.json()['last_name'], 'only')
        self.assertEqual(response.json()['is_superuser'], False)

    def test_get_is_admin(self):
        """
        Submits a POST request
        """
        response = self.rpgt_api_cli.get(API_URL + 'is-admin',
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_post_token(self):
        """
        Submits a POST request against MODEL_URL
        Validates admin access
        """
        response = self.rpgt_api_cli.post(T_URL,
                                          RO_USER,
                                          format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertTrue(response.json()['access'])

    def test_post_token_refresh(self):
        """
        Submits a POST request against MODEL_URL
        Validates admin access
        """
        response = self.rpgt_api_cli.post(T_URL + '/refresh',
                                          {"refresh": self.refresh},
                                          format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertTrue(response.json()['access'])

    def test_post_token_verify(self):
        """
        Submits a POST request against MODEL_URL
        Validates admin access
        """
        response = self.rpgt_api_cli.post(T_URL + '/refresh/',
                                          {"token": self.token},
                                          format="json")
        self.assertEqual(response.status_code, CODES["success"])
        self.assertFalse(response.json())


@tag("views_anonymous")
class TestsAnonymous(RpgtApiBTC):
    """
    Defines TestsAnonymous class
    """

    def test_get_current_user(self):
        """
        test_get_current_user
        """
        response = self.rpgt_api_cli.get(API_URL + 'current-user')
        self.assertEqual(response.status_code, CODES["success"])
        self.assertEqual(response.json()['is_authenticated'], False)
        self.assertEqual(response.json()['username'], None)
        self.assertEqual(response.json()['first_name'], None)
        self.assertEqual(response.json()['last_name'], None)
        self.assertEqual(response.json()['is_superuser'], None)

    def test_get_is_admin(self):
        """
        test_get_is_admin
        """
        response = self.rpgt_api_cli.get(API_URL + 'is-admin')
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_get_info(self):
        """
        test_get_info
        """
        response = self.rpgt_api_cli.get(API_URL + 'info')
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_token_failure(self):
        """
        test_post_token_failure
        """
        response = RpgtApiBTC.rpgt_api_cli.post(T_URL,
                                                {"username": "foo",
                                                 "password": "bar"},
                                                format="json")
        self.assertEqual(response.status_code, CODES["no_creds"])

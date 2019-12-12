"""
Base module for all tests
"""
from django.test import TestCase
from django.test.utils import override_settings
from rest_framework.test import APIClient

@override_settings(AUTHENTICATION_BACKENDS=('django.contrib.auth.backends.ModelBackend',))
class RPGToolsApiBaseTestCase(TestCase):
    """
    http://jmoiron.net/blog/subclassing-djangos-testcase/
    """
    rpgtools_api_client = APIClient()
    rpgtools_api_client_ro = APIClient()

    def _pre_setup(self):
        admin_token = self.rpgtools_api_client.post('/api/v1/token',
                                                    {"username": "admin",
                                                     "password": "adminpass"},
                                                    format="json").json()["access"]
        self.rpgtools_api_client(
            HTTP_AUTHORIZATION=f"Bearer {admin_token}"
        )

        ro_token = self.rpgtools_api_client_ro('/api/v1/token',
                                               {"username": "read-only",
                                                "password": "ropassword"},
                                               format="json").json()["access"]

        self.rpgtools_api_client_ro.credentials(
            HTTP_AUTHORIZATION=f"Bearer {ro_token}")

        super(RPGToolsApiBaseTestCase, self)._pre_setup()

    def _post_teardown(self):
        super(RPGToolsApiBaseTestCase, self)._post_teardown()

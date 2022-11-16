# -*- coding: utf-8 -*-
# TODO: break out into individual files under api/tests/book
"""Defines test case run against the API for the Book model
"""
from django.test import tag
from api.tests.base import RpgtApiBTC
from api.tests.base import ADMIN_USER
from api.tests.base import API_URL
from api.tests.base import CODES
from api.tests.base import RO_USER
from api.tests.base import T_URL

MODEL_URL = API_URL + 'books'
POST_URL = MODEL_URL + '/'
EDIT_URL = POST_URL + 'edit/'
DELETE_URL = POST_URL + 'delete/'

INSTANCE_ID = 'going-home'
GET_COUNT = 4

FIXTURES = ['test_users',
            'test_book.json',
            'test_bookformat.json',
            'test_contributor.json',
            'test_game.json',
            'test_gamesystem.json',
            'test_publisher.json', ]

CREATE_TEST_VALUE = 'test-book'
TEST_VALUE = 'UPDATED VIA TESTS'

REQUEST_DATA_CREATE = {
    "name": "Test Book",
    "description": "Test book",
    "read_me": "Test Book==---A test book",
    "url": "https://www.google.com",
    "book_format": "5824260c-36f6-4196-8403-80c558ffff08",
    "publisher": "c7348e4d-9145-421e-ab19-d5eda71a757d",
    "short_name": "Going Home",
    "abbreviation": "GH",
    "catalog_number": "506",
    "pages": 40,
    "publication_year": 1986,
    "isbn_10": "0943580560",
    "isbn_13": "9780943580562",
    "game": [
        "9d739130-b037-4425-8103-3cf13bd21fc1"
    ],
    "art_assistant": [],
    "art_director": [
        "9f6fba93-9955-4a52-99be-647e9bf58346",
        "204cdcad-a648-4db7-ba1f-039000c00ebf"
    ],
    "artist_cover": [
        "cb4f7eb6-69bc-4df6-b6ce-73f67d6a1a52"
    ],
    "artist_interior": [
        "cc4704ef-261b-432d-82ce-e88a7ace7615"
    ],
    "author": [],
    "designer": [
        "ce78c288-421b-42ec-8d83-8f84f0f29dc8"
    ],
    "developer": [],
    "editor": [],
    "graphic_designer": [],
    "play_tester": [],
    "proofreader": [],
    "research_assistant": [
        "c9c36bcf-d2b6-47c5-927c-f67970df5d03",
        "66efafd4-f5a4-4668-acb7-0ceeff949d32"
    ],
    "text_manager": [],
    "text_processor": [],
    "type_setter": []
}

REQUEST_DATA_CREATE_DUPLICATE = {
    "name": "Going Home",
    "description": "A game module for use with GDW's World War III role-playing game, Twilight: 2000.",  # pylint: disable=line-too-long
    "read_me": "Going Home\n==\n---\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_It came as quite a surprise when we finally confirmed it. What remained of the big brass in Europe decided that it was time for everyone to get out of the pool, so they arranged for a few ships to take us back to America. Problem was, nobody believed that the ships would have enough room for everybody. We decided that this was the last ride going our way, and it was time to go home. The ships were leaving on November 15, and there were no reserved seats...what with thirty or forty thousand people looking for seats, it could get to be quite a game of musical chairs._\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Going Home_ is an adventure for use with GDW's World War III role-playing game, **Twilight: 2000**. In _Going Home_, the players are presented with the challenge with getting across most of Poland and north-central Germany to catch the last ship heading back to the US for quite a while.\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Even if the players choose to remain in Europe, _Going Home_ will still be of tremendous interest. The adventure contains:<ul><li>A full-color pull-out map, covering northern Germany which overlaps with the full-color Poland map included in the original game.</li><li>A referee's update of the location and strength of NATO and Warsaw Pact units in their winter quarters as the year 2000draws to a close.</li><li>A brief rundown of French units in the occupied area west of the Rhine and a discussion of French military activities in the so-called \\\"dead zone\\\" east of the Rhine. Also, a bonus: read_mes (in _Twilight: 2000_ terms of three French helicopters.</li><li>Details and specifications, in _Twilight: 2000_ terms, the German Leopard III and the British Challenger tanks, and British 120mm rifled gun.</li></ul>",  # pylint: disable=line-too-long
    "url": "",
    "book_format": "5824260c-36f6-4196-8403-80c558ffff08",
    "publisher": "c7348e4d-9145-421e-ab19-d5eda71a757d",
    "short_name": "Going Home",
    "abbreviation": "GH",
    "catalog_number": "506",
    "pages": 40,
    "publication_year": 1986,
    "isbn_10": "0943580560",
    "isbn_13": "9780943580562",
    "game": [
        "9d739130-b037-4425-8103-3cf13bd21fc1"
    ],
    "art_assistant": [],
    "art_director": [
        "9f6fba93-9955-4a52-99be-647e9bf58346",
        "204cdcad-a648-4db7-ba1f-039000c00ebf"
    ],
    "artist_cover": [
        "cb4f7eb6-69bc-4df6-b6ce-73f67d6a1a52"
    ],
    "artist_interior": [
        "cc4704ef-261b-432d-82ce-e88a7ace7615"
    ],
    "author": [],
    "designer": [
        "ce78c288-421b-42ec-8d83-8f84f0f29dc8"
    ],
    "developer": [],
    "editor": [],
    "graphic_designer": [],
    "play_tester": [],
    "proofreader": [],
    "research_assistant": [
        "c9c36bcf-d2b6-47c5-927c-f67970df5d03",
        "66efafd4-f5a4-4668-acb7-0ceeff949d32"
    ],
    "text_manager": [],
    "text_processor": [],
    "type_setter": []
}

REQUEST_DATA_PATCH = {
    "description": TEST_VALUE,
}

REQUEST_DATA_PUT = {
    "name": "Going Home",
    "description": TEST_VALUE,
    "read_me": "Going Home\n==\n---\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_It came as quite a surprise when we finally confirmed it. What remained of the big brass in Europe decided that it was time for everyone to get out of the pool, so they arranged for a few ships to take us back to America. Problem was, nobody believed that the ships would have enough room for everybody. We decided that this was the last ride going our way, and it was time to go home. The ships were leaving on November 15, and there were no reserved seats...what with thirty or forty thousand people looking for seats, it could get to be quite a game of musical chairs._\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Going Home_ is an adventure for use with GDW's World War III role-playing game, **Twilight: 2000**. In _Going Home_, the players are presented with the challenge with getting across most of Poland and north-central Germany to catch the last ship heading back to the US for quite a while.\n\n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Even if the players choose to remain in Europe, _Going Home_ will still be of tremendous interest. The adventure contains:<ul><li>A full-color pull-out map, covering northern Germany which overlaps with the full-color Poland map included in the original game.</li><li>A referee's update of the location and strength of NATO and Warsaw Pact units in their winter quarters as the year 2000draws to a close.</li><li>A brief rundown of French units in the occupied area west of the Rhine and a discussion of French military activities in the so-called \\\"dead zone\\\" east of the Rhine. Also, a bonus: read_mes (in _Twilight: 2000_ terms of three French helicopters.</li><li>Details and specifications, in _Twilight: 2000_ terms, the German Leopard III and the British Challenger tanks, and British 120mm rifled gun.</li></ul>",  # pylint: disable=line-too-long
    "url": "",
    "book_format": "5824260c-36f6-4196-8403-80c558ffff08",
    "publisher": "c7348e4d-9145-421e-ab19-d5eda71a757d",
    "short_name": "Going Home",
    "abbreviation": "GH",
    "catalog_number": "506",
    "pages": 40,
    "publication_year": 1986,
    "isbn_10": "0943580560",
    "isbn_13": "9780943580562",
    "game": [
        "9d739130-b037-4425-8103-3cf13bd21fc1"
    ],
    "art_assistant": [],
    "art_director": [
        "9f6fba93-9955-4a52-99be-647e9bf58346",
        "204cdcad-a648-4db7-ba1f-039000c00ebf"
    ],
    "artist_cover": [
        "cb4f7eb6-69bc-4df6-b6ce-73f67d6a1a52"
    ],
    "artist_interior": [
        "cc4704ef-261b-432d-82ce-e88a7ace7615"
    ],
    "author": [],
    "designer": [
        "ce78c288-421b-42ec-8d83-8f84f0f29dc8"
    ],
    "developer": [],
    "editor": [],
    "graphic_designer": [],
    "play_tester": [],
    "proofreader": [],
    "research_assistant": [
        "c9c36bcf-d2b6-47c5-927c-f67970df5d03",
        "66efafd4-f5a4-4668-acb7-0ceeff949d32"
    ],
    "text_manager": [],
    "text_processor": [],
    "type_setter": []
}


@tag("book_admin")
class TestAdmin(RpgtApiBTC):
    """
    Defines book test case class
    """
    fixtures = FIXTURES
    token = RpgtApiBTC.rpgt_api_cli.post(T_URL,
                                         ADMIN_USER,
                                         format="json").json()["access"]

    # admin user operations
    def test_get_item(self):
        """
        Submits a GET request against MODEL_URL
        """
        response = self.rpgt_api_cli.get(MODEL_URL,
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(len(response.json()), GET_COUNT)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID
        """
        response = self.rpgt_api_cli.get(POST_URL + INSTANCE_ID,
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['id'], INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id_history(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/history'
        """
        response = self.rpgt_api_cli.get(POST_URL + INSTANCE_ID + '/history',
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertTrue(response.json())
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_item(self):
        """
        Submits a POST request against POST_URL
        """
        response = self.rpgt_api_cli.post(POST_URL,
                                          REQUEST_DATA_CREATE,
                                          format="json",
                                          HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['id'], CREATE_TEST_VALUE)
        self.assertEqual(response.status_code, CODES["created"])

        response = self.rpgt_api_cli.patch(EDIT_URL + CREATE_TEST_VALUE,
                                           REQUEST_DATA_PATCH,
                                           format="json",
                                           HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['description'], TEST_VALUE)
        self.assertEqual(response.status_code, CODES["success"])

        response = self.rpgt_api_cli.get(POST_URL + CREATE_TEST_VALUE + '/history',
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertTrue(response.json())
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_duplicate_item(self):
        """
        Submits a POST request against POST_URL
        Attemptes to create a duplicate instance
        """
        response = self.rpgt_api_cli.post(POST_URL,
                                          REQUEST_DATA_CREATE_DUPLICATE,
                                          format="json",
                                          HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["bad_request"])

    def test_patch_item(self):
        """
        Submits a PATCH request against EDIT_URL + INSTANCE_ID
        """
        response = self.rpgt_api_cli.patch(EDIT_URL + INSTANCE_ID,
                                           REQUEST_DATA_PATCH,
                                           format="json",
                                           HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['description'], TEST_VALUE)
        self.assertEqual(response.status_code, CODES["success"])

    def test_put_item(self):
        """
        Submits a PUT request against EDIT_URL + INSTANCE_ID
        """
        response = self.rpgt_api_cli.put(EDIT_URL + INSTANCE_ID,
                                         REQUEST_DATA_PUT,
                                         format="json",
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['description'], TEST_VALUE)
        self.assertEqual(response.status_code, CODES["success"])

    def test_delete_item(self):
        """
        Submits a DELETE request against DELETE_URL + INSTANCE_ID
        """
        response = self.rpgt_api_cli.delete(DELETE_URL + INSTANCE_ID,
                                            HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["deleted"])


@tag("book_readonly")
class BookFormatTestReadOnly(RpgtApiBTC):
    """
    Defines book test case class
    """
    fixtures = FIXTURES
    token = RpgtApiBTC.rpgt_api_cli.post(T_URL,
                                         RO_USER,
                                         format="json").json()["access"]

    # read-only user operations
    def test_get_item(self):
        """
        Submits a GET request against POST_URL
        Uses read-only creds
        """
        response = self.rpgt_api_cli.get(MODEL_URL,
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(len(response.json()), GET_COUNT)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID
        Uses read-only creds
        """
        response = self.rpgt_api_cli.get(POST_URL + INSTANCE_ID,
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.json()['id'], INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id_history(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/history'
        Uses read-only creds
        """
        response = self.rpgt_api_cli.get(POST_URL + INSTANCE_ID + '/history',
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertTrue(response.json())
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_item(self):
        """
        Submits a POST request against POST_URL
        Uses read-only creds
        """
        response = self.rpgt_api_cli.post(POST_URL,
                                          REQUEST_DATA_CREATE,
                                          format="json",
                                          HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_patch_item(self):
        """
        Submits a PATCH request against EDIT_URL + INSTANCE_ID
        Uses read-only creds
        """
        response = self.rpgt_api_cli.patch(EDIT_URL + INSTANCE_ID,
                                           REQUEST_DATA_PATCH,
                                           format="json",
                                           HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_put_item(self):
        """
        Submits a PUT request against EDIT_URL + INSTANCE_ID
        USES read-only creds
        """
        response = self.rpgt_api_cli.put(EDIT_URL + INSTANCE_ID,
                                         REQUEST_DATA_PUT,
                                         format="json",
                                         HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])

    def test_delete_item(self):
        """
        Submits a DELETE request against DELETE_URL + INSTANCE_ID
        Uses read-only creds
        """
        response = self.rpgt_api_cli.delete(DELETE_URL + INSTANCE_ID,
                                            HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(response.status_code, CODES["no_permission"])


@tag("book_anonymous")
class TestAnonymous(RpgtApiBTC):
    """
    Defines book test case class
    """
    fixtures = FIXTURES

    # anonymous user operations
    def test_get_item(self):
        """
        Submits a GET request against POST_URL
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.get(MODEL_URL)
        self.assertEqual(len(response.json()), GET_COUNT)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.get(POST_URL + INSTANCE_ID)
        self.assertEqual(response.json()['id'], INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["success"])

    def test_get_item_id_history(self):
        """
        Submits a GET request against POST_URL + INSTANCE_ID + '/history'
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.get(POST_URL + INSTANCE_ID + '/history')
        self.assertTrue(response.json())
        self.assertEqual(response.status_code, CODES["success"])

    def test_post_item(self):
        """
        Submits a POST request against POST_URL
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.post(POST_URL,
                                          REQUEST_DATA_CREATE,
                                          format="json")
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_patch_item(self):
        """
        Submits a PATCH request against EDIT_URL + INSTANCE_ID
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.patch(EDIT_URL + INSTANCE_ID,
                                           REQUEST_DATA_PATCH,
                                           format="json")
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_put_item(self):
        """
        Submits a PUT request against EDIT_URL + INSTANCE_ID
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.put(EDIT_URL + INSTANCE_ID,
                                         REQUEST_DATA_PUT,
                                         format="json")
        self.assertEqual(response.status_code, CODES["no_creds"])

    def test_delete_item(self):
        """
        Submits a DELETE request against DELETE_URL + INSTANCE_ID
        Uses anonymouse access
        """
        response = self.rpgt_api_cli.delete(DELETE_URL + INSTANCE_ID)
        self.assertEqual(response.status_code, CODES["no_creds"])

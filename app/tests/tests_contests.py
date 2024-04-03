from http import HTTPStatus

import pytest
import requests

from app import CONTESTS, USERS
from app.tests import ENDPOINT


@pytest.fixture
def create_contest_payload():

    return {
        "name": "name" + str(len(CONTESTS)),
        "sport": "sport" + str(len(CONTESTS)),
        "participants": [0],
        "start_date": "2020-01-10",
        "end_date": "2020-01-20",
    }


def create_user_payload():
    return {
        "first_name": "name" + str(len(USERS)),
        "last_name": "lastname" + str(len(USERS)),
        "email": "email@test.ru",
        "sport": "sport" + str(len(USERS)),
    }


def test_create_contest(create_contest_payload):
    payload_contest = create_contest_payload
    payload_user = create_user_payload()

    requests.post(f"{ENDPOINT}/user/create", json=payload_user)
    response = requests.post(f"{ENDPOINT}/contest/create", json=payload_contest)

    assert response.status_code == HTTPStatus.CREATED


def test_get_contest(create_contest_payload):
    payload_contest = create_contest_payload
    payload_user = create_user_payload()

    requests.post(f"{ENDPOINT}/user/create", json=payload_user)
    requests.post(f"{ENDPOINT}/contest/create", json=payload_contest)

    expected_response = {
        "contest_id": 0,
        "name": "name0",
        "sport": "sport0",
        "participants": [0],
        "start_date": "2020-01-10",
        "end_date": "2020-01-20",
        "status": "Started",
        "winner": None,
    }

    response = requests.get(f"{ENDPOINT}/contest/0")
    assert response.json() == expected_response

from http import HTTPStatus

import pytest
import requests

from app import USERS
from app.tests import ENDPOINT


count_users = 0


@pytest.fixture
def create_user_payload():
    return {
        "first_name": "name" + str(len(USERS)),
        "last_name": "lastname" + str(len(USERS)),
        "email": "email@test.ru",
        "sport": "sport" + str(len(USERS)),
    }


def test_user_create(create_user_payload):
    global count_users
    payload = create_user_payload
    create_response = requests.post(f"{ENDPOINT}/user/create", json=payload)
    assert create_response.status_code == HTTPStatus.CREATED
    count_users += 2
    payload = create_user_payload
    create_response = requests.post(f"{ENDPOINT}/user/create", json=payload)

    post_data = create_response.json()
    user_id = post_data["user_id"]
    expected = {
        "user_id": 1,
        "first_name": "name0",
        "last_name": "lastname0",
        "email": "email@test.ru",
        "sport": "sport0",
    }

    assert post_data == expected

    get_response = requests.get(f"{ENDPOINT}/user/{user_id}")
    get_data = get_response.json()
    expected = {
        "user_id": 1,
        "first_name": "name0",
        "last_name": "lastname0",
        "email": "email@test.ru",
        "sport": "sport0",
        "contests": [],
    }
    assert get_data == expected


def test_user_create_wrong_email(create_user_payload):
    payload = create_user_payload
    payload["email"] = "wrong_email"
    create_response = requests.post(f"{ENDPOINT}/user/create", json=payload)
    assert create_response.status_code == HTTPStatus.BAD_REQUEST


def test_user_contests():
    payload = {
        "name": "name1",
        "sport": "sport1",
        "participants": [0],
        "start_date": "2020-01-10",
        "end_date": "2020-01-20",
    }
    requests.post(f"{ENDPOINT}/contest/create", json=payload)
    get_response = requests.get(f"{ENDPOINT}/users/0/contests")
    expected_response = [
        dict(
            {
                "contest_id": 0,
                "name": "name1",
                "sport": "sport1",
                "participants": [0],
                "start_date": "2020-01-10",
                "end_date": "2020-01-20",
                "status": "Started",
                "winner": None,
            }
        )
    ]
    # print(get_response.json()["contests"])

    assert get_response.json()["contests"] == expected_response


def test_get_users_leaderboard(create_user_payload):
    global count_users
    n = 5
    for _ in range(n):
        payload = create_user_payload
        create_response = requests.post(f"{ENDPOINT}/user/create", json=payload)
        assert create_response.status_code == HTTPStatus.CREATED
        count_users += 1

    leaderboard_payload = {"type": "list", "sort": "ascending"}

    get_response = requests.get(
        f"{ENDPOINT}/users/leaderboard", json=leaderboard_payload
    )
    leaderboard = get_response.json()["users"]
    assert isinstance(leaderboard, list)
    assert len(leaderboard) == count_users

from app import app, USERS, models, CONTESTS, StringConst
from flask import request, Response
import json
from http import HTTPStatus
import matplotlib.pyplot as plt


@app.post("/user/create")
def user_create():
    data = request.get_json()
    user_id = len(USERS)
    first_name = data["first_name"]
    last_name = data["last_name"]
    email = data["email"]
    sport = data["sport"]
    if not (models.User.validate_email(email)):
        return Response(status=HTTPStatus.BAD_REQUEST)
    user_created = models.User(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        sport=sport,
    )

    USERS[user_id] = user_created
    response = Response(
        json.dumps(
            {
                "user_id": user_created.user_id,
                "first_name": user_created.first_name,
                "last_name": user_created.last_name,
                "email": user_created.email,
                "sport": user_created.sport,
            }
        ),
        HTTPStatus.CREATED,
        mimetype="application/json",
    )
    return response


@app.get("/user/<int:user_id>")
def get_user(user_id):
    if not (user_id in USERS):
        return Response(status=HTTPStatus.NOT_FOUND)
    response = Response(
        json.dumps(USERS[user_id].to_dict()),
        HTTPStatus.OK,
        mimetype="application/json",
    )
    return response


@app.get("/users/<int:user_id>/contests")
def get_user_contests(user_id):
    if not (user_id in USERS):
        return Response(status=HTTPStatus.NOT_FOUND)
    user = USERS[user_id]
    response = Response(
        json.dumps(
            {
                "contests": [
                    CONTESTS[contest_id].to_dict() for contest_id in user.contests
                ]
            }
        ),
        HTTPStatus.OK,
        mimetype="application/json",
    )
    return response


@app.get("/users/leaderboard")
def get_leaderboard():
    data = request.json
    type = data["type"]

    if type == StringConst.list.value:
        sort_users = data["sort"]
        if sort_users == StringConst.ascending.value:
            leaderboard = [
                user.to_dict() for user in sorted(USERS.values(), reverse=False)
            ]
        elif sort_users == StringConst.descending.value:
            leaderboard = [
                user.to_dict() for user in sorted(USERS.values(), reverse=True)
            ]
        else:
            return Response(status=HTTPStatus.NOT_IMPLEMENTED)
        response = Response(
            json.dumps({"users": leaderboard}),
            HTTPStatus.OK,
            mimetype="application/json",
        )
        return response
    elif type == StringConst.graph.value:
        leaderboard = USERS

        fig, ax = plt.subplots()

        sportsman = [f"{user.first_name} {user.last_name}" for user in leaderboard]
        count_contests = [len(user.contests) for user in leaderboard]
        ax.bar(sportsman, count_contests)

        ax.set_ylabel("Count of Contests")
        ax.set_title("User leaderboard by contest")

        plt.savefig("leaderboard.png")
        return Response("<img src='leaderboard.png'")

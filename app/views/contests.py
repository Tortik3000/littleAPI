from app import app, USERS, models, CONTESTS
from flask import request, Response
import json
from http import HTTPStatus


@app.post("/contest/create")
def create_contest():
    data = request.get_json()
    contest_id = len(CONTESTS)
    name = data["name"]
    sport = data["sport"]
    participants = data["participants"]
    start_date = data["start_date"]
    end_date = data["end_date"]

    for participant in participants:
        if int(participant) in USERS:
            for user in USERS.values():
                if user.user_id == int(participant):
                    user.add_contest(contest_id)
        else:
            return Response(status=HTTPStatus.NOT_FOUND)

    contest_created = models.Contest(
        contest_id=contest_id,
        name=name,
        sport=sport,
        participants=participants,
        start_date=start_date,
        end_date=end_date,
    )

    CONTESTS.append(contest_created)
    response = Response(
        json.dumps(contest_created.to_dict()),
        HTTPStatus.CREATED,
        mimetype="application/json",
    )
    return response


@app.get("/contest/<int:contest_id>")
def get_contest(contest_id):
    if contest_id < 0 or contest_id > len(CONTESTS):
        return Response(status=HTTPStatus.NOT_FOUND)
    contest = CONTESTS[contest_id]
    response = Response(
        json.dumps(contest.to_dict()),
        HTTPStatus.OK,
        mimetype="application/json",
    )
    return response


@app.post("/contest/<int:contest_id>/finish")
def finish_contest(contest_id):
    data = request.get_json()
    winner = data["winner"]
    if not (winner in USERS):
        return Response(status=HTTPStatus.NOT_FOUND)

    contest = CONTESTS[contest_id]
    contest.finish(winner)

    response = Response(
        json.dumps(contest.to_dict()),
        HTTPStatus.OK,
        mimetype="application/json",
    )
    return response

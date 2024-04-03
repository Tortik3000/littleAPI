import re
from app import StringConst


class User:
    def __init__(self, user_id, first_name, last_name, email, sport):
        self.contests = []
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.sport = sport

    @staticmethod
    def validate_email(email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False

    def add_contest(self, contest):
        self.contests.append(contest)

    def __lt__(self, other):
        return len(self.contests) < len(other.contests)

    def to_dict(self):
        return dict(
            {
                "user_id": self.user_id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
                "sport": self.sport,
                "contests": self.contests,
            }
        )

    def to_string(self):
        return (
            f"user_id: {self.user_id},<br>"
            f"first_name: {self.first_name},<br>"
            f"last_name: {self.last_name},<br>"
            f"email: {self.email},<br>"
            f"sport: {self.sport},<br>"
            f"contests: {self.contests},<br>"
        )


class Contest:
    def __init__(self, contest_id, name, sport, participants, start_date, end_date):
        self.contest_id = contest_id
        self.name = name
        self.participants = participants
        self.sport = sport
        self.start_date = start_date
        self.end_date = end_date
        self.status = StringConst.started.value
        self.winner = None

    def finish(self, winner):
        self.winner = winner
        self.status = StringConst.finished.value

    def add_participant(self, participant):
        self.participants.append(participant)

    def to_dict(self):
        return dict(
            {
                "contest_id": self.contest_id,
                "name": self.name,
                "sport": self.sport,
                "participants": self.participants,
                "start_date": self.start_date,
                "end_date": self.end_date,
                "status": self.status,
                "winner": self.winner,
            }
        )

    def to_string(self):
        return (
            f"contest_id: {self.contest_id},<br>"
            f"name: {self.name},<br>"
            f"sport: {self.sport},<br>"
            f"participants: {self.participants},<br>"
            f"status: {self.status},<br>"
            f"winner: {self.winner}<br>"
        )

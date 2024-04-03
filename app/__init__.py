from flask import Flask
from enum import StrEnum

app = Flask(__name__)

USERS = dict()
CONTESTS = []


class StringConst(StrEnum):
    list = ("list",)
    graph = ("graph",)
    ascending = ("ascending",)
    descending = ("descending",)
    started = ("Started",)
    finished = ("Finished",)


from app import views_all
from app import models
from app import views
from app import tests

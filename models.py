#  Title:   models.py
#  Desc:    This is a shitty ass python file filled with classes that act as objects
#           to be instantiated when extracting info about posts and users.
#  Author:  Angela Louise Trainor
#  Date:    03/28/2026

from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: str
    following: list  # list of user IDs
    interests: list  # topic tags

@dataclass
class Post:
    id: str
    author_id: str
    content: str
    timestamp: datetime
    likes: int
    replies: int
    reposts: int
    topic: str

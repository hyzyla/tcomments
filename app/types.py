from typing import NamedTuple, List

from app.models import Comment


class GroupedComment(NamedTuple):
    parent: Comment
    children: List['GroupedComment']

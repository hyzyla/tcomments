import uuid

from sqlalchemy.dialects import postgresql
import sqlalchemy as sa

from app import db


def uuid_type():
    return postgresql.UUID(as_uuid=False)


def gen_uuid():
    return str(uuid.uuid4())


class ID(db.Column):
    def __init__(self):
        super().__init__(
            uuid_type(),
            primary_key=True,
            default=gen_uuid,
        )


class Text(db.Column):
    def __init__(self, nullable: bool = False):
        super().__init__(db.Text, nullable=nullable)


class ForeignID(db.Column):

    def __init__(self, reference: str, nullable: bool = False):
        super().__init__(uuid_type(), db.ForeignKey(reference), nullable=nullable)


class DateTime(db.Column):
    def __init__(self, nullable: bool = False):
        super().__init__(db.DateTime, nullable=nullable)


class JSON(db.Column):
    def __init__(self, nullable: bool = False):
        super().__init__(db.JSON, nullable=nullable)
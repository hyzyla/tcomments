from sqlalchemy.dialects import postgresql
import sqlalchemy as sa

from app import db


def uuid_type():
    return postgresql.UUID(as_uuid=False)


class ID(db.Column):
    def __init__(self):
        super().__init__(
            uuid_type(),
            primary_key=True,
            server_default=sa.text("uuid_generate_v4()")
        )


class Text(db.Column):
    def __init__(self):
        super().__init__(db.Text)


class ForeignID(db.Column):

    def __init__(self, reference: str, nullable: bool = False):
        super().__init__(uuid_type(), db.ForeignKey(reference), nullable=nullable)

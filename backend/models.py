from sqlalchemy import Column, Integer, String, Text, DateTime
from backend.database import Base


class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    body = Column(Text)

    def to_dict(self):
        return dict(
            id=self.id,
            body=self.body
        )

    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return 'id={0}, body={1}'.format(self.id, self.body)
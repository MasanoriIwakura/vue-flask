from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func
import os
import backend.models


database_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../flask.db')
engine = create_engine('sqlite:///' + database_file, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)

def insertTodo(todo):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(todo)
    session.commit()
    session.close()

def deleteTodo(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    todo = session.query(backend.models.Todo).get(id)
    session.delete(todo)
    session.commit()
    session.close()

def selectAllTodo():
    print('*** select all todo ***')
    Session = sessionmaker(bind=engine)
    session = Session()
    todos = session.query(backend.models.Todo).all()
    session.close()
    return todos

def selectMaxIdForTodo():
    Session = sessionmaker(bind=engine)
    session = Session()
    max = session.query(func.max(backend.models.Todo.id)).scalar()
    session.close()
    return max

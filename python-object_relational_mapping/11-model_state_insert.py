#!/usr/bin/python3
"""Script that adds a new State oject to the table"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    vroom = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=vroom)
    session = Session()

    Lousianne = State(name='Louisiana')

    session.add(Lousianne)
    session.commit()

    da_state = session.query(State).order_by(State.id.desc()).first()

    if da_state is None:
        print("Nothing")
    else:
        print(f"{da_state.id}")

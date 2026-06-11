#!/usr/bin/python3
"""Script that prints the states with an 'a'"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":

    vroom = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                argv[1], argv[2], argv[3]),
            pool_pre_ping=True)

    Base.metadata.bind = vroom
    Session = sessionmaker(bind=vroom)
    session = Session()

    da_state = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in da_state:
        print("{}: {}".format(state.id, state.name))

    session.close()

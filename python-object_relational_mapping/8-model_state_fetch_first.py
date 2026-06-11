#!/usr/bin/python3
"""Script that prints the first State object from the db"""

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

    da_state = session.query(State).order_by(State.id).first()

    if da_state is None:
        print("Nothing")
    else:
        print(f"{da_state.id}: {da_state.name}")

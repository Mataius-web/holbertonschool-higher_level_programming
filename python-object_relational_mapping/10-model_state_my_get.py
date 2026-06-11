#!/usr/bin/python3
"""Script that fetches a data from a given input by the user"""
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

    da_state = session.query(State).filter(
        State.name == argv[4]).first()

    if da_state is None:
        print("Not found")
    else:
        print(da_state.id)

    session.close()

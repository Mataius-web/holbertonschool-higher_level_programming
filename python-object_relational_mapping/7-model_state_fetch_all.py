#!/usr/bin/python3
"""Query to fetch all the states using SQL alchemy"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for da_state in session.query(State).order_by(State.id):
        print(f"{da_state.id}: {da_state.name}")

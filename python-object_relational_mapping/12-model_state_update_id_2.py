#!/usr/bin/python3
"""Script that updates a data using the ORM"""

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

    upd_state = session.query(State).filter_by(id=2).first()

    upd_state.name = "New Mexico"
    session.commit()

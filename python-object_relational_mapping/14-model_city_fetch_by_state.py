#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    vroom = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=vroom)
    session = Session()

    for da_states, da_cities in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id).all():

        print("{}: ({}) {}".format(
            da_states.name, da_cities.id, da_cities.name))

#!/usr/bin/python3
# Get all states
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from relationship_state import State
from relationship_city import Base, City


import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
        )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for ins_state in session.query(State).order_by(State.id):
        for ins_city in ins_state.cities:
            print('{}: {} -> {}'.format(
                ins_city.id, ins_city.name, ins_state.name))

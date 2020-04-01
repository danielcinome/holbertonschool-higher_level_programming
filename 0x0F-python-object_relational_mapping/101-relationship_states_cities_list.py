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
        print('{}: {}'.format(ins_state.id, ins_state.name))
        for ins_city in session.query(City).filter(
                ins_state.id == City.state_id).order_by(City.id):
            print('\t{}: {}'.format(ins_city.id, ins_city.name))

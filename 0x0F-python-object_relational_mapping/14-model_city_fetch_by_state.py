#!/usr/bin/python3
# States -Cities
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
        )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    for ins_state in session.query(State).order_by(State.id):
        for ins_city in session.query(City)\
        .filter(ins_state.id == City.state_id).order_by(City.id):
            print('{}: ({}) {}'.format(
                ins_state.name, ins_city.id, ins_city.name))

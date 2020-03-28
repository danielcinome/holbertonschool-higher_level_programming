#!/usr/bin/python3
# Get all states
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
        )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    try:
        instance = session.query(State).filter(
            State.id == 1).order_by(State.id).one()
        print('{}: {}'.format(instance.id, instance.name))
    except:
        print('Nothing')

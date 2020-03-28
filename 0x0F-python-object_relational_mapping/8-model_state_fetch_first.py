#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""
if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()
    for state in session.query(State).order_by(State.id)[0:1]:
        print("{}: {}".format(state.id, state.name))
    session.close()
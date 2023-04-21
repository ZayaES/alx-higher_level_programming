#!/usr/bin/python3
"""Connects to a dtabase and prints thr table states"""

if __name__ == "__main__":
    from sqlalchemy import Integer, String, MetaData, create_engine
    from sqlalchemy.orm import Session, sessionmaker
    import sys
    from model_state import Base, State

    user = sys.argv[1]
    passwd = sys.argv[2]
    dbase = sys.argv[3]
    s_state = sys.argv[4]
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                user, passwd, dbase))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name.in_([s_state])).all()
    try:
        f = state[0]
        for occ in state:
            print("{}".format(occ.id))
    except IndexError:
        print("Not found")

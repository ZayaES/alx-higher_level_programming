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
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                user, passwd, dbase))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State).first()
    if q:
        print("1: {}".format(q))
    else:
        print("Nothing")

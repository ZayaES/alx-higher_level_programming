#!/usr/bin/python3
"""Connects to a dtabase and prints thr table states"""

if __name__ == "__main__":
    from sqlalchemy import Integer, String, MetaData, create_engine
    from sqlalchemy.orm import Session, sessionmaker
    import sys
    from model_state import Base, State
    from model_city import City

    user = sys.argv[1]
    passwd = sys.argv[2]
    dbase = sys.argv[3]
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                user, passwd, dbase))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).filter(
            City.state_id==State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

#!/usr/bin/python3

if __name__ == "__main__":
    from sqlalchemy import Integer, String, MetaData, create_engine
    from sqlalchemy.orm import Session, sessionmaker
    import sys
    from model_state import Base, State

    user = sys.argv[1]
    print(user)
    passwd = sys.argv[2]
    dbase = sys.argv[3]
    print(dbase)
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                user, passwd, dbase))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).all():
        print("{}: {}".format(state.id, state.name))

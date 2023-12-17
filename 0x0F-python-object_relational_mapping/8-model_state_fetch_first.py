#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sess = Session()

    instance = sess.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(f"{instance.id}: {instance.name}")

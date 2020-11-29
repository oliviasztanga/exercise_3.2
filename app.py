from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from seed import seed


DATABASE_URI = 'postgres+psycopg2://localhost:5432/zoo'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)


def refresh_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # seed(Session()) # uncomment to demo seed example

if __name__ == '__main__':
    refresh_database()
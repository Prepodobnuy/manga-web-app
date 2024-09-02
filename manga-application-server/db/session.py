from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


def get_engine():
    url = f"sqlite:///./db.db"
    if not database_exists(url):
        create_database(url)
    
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

def get_engine_from_settings():
    return get_engine()

def get_session_engine():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    return session, engine
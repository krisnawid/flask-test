
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from config import Config

def test_database_connection():
    db_uri = Config.SQLALCHEMY_DATABASE_URI
    engine = create_engine(db_uri)

    try:
        with engine.connect():
            print("Connection to the database successful!")
    except OperationalError as e:
        print(f"Failed to connect to the database. Error: {str(e)}")

if __name__ == "__main__":
    test_database_connection()
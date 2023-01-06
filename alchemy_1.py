"""
to use password containing @, in the connection string -

from urllib import parse
engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{db}".format(
    user="root",
    password=parse.quote("Ash@95kh"),
    host="localhost",
    db="starwarsdb2"
    )
)
"""
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.sql import select, insert, delete


def get_connection():
    user = "root"
    password = "Ash95kh"
    host = "localhost"
    database = "starwarsdb2"

    engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{db}".format(
        user=user,
        password=password,
        host=host,
        db=database
        )
    )
    print(f"Connection to the {host} for user {user} created successfully.")
    meta_data = db.MetaData()
    # engine = create_engine("""mysql+pymysql://root:"Ash@95kh"@localhost/starwarsdb2""")
    # connection = engine.connect()
    return engine, meta_data


def create_profile():
    engine, meta_data = get_connection()
    profile_ = db.Table(
        "profile",
        meta_data,
        db.Column("id", db.Integer, primary_key=True),
        db.Column("name", db.String(250)),
        db.Column("email", db.String(250)),
        db.Column("contact", db.BigInteger)
    )
    meta_data.create_all(engine)
    return profile_


def select_profile(profile):
    engine, _ = get_connection()
    s = select(profile)
    result = engine.execute(s)
    return result


def insert_profile(profile):
    engine, meta_data = get_connection()
    stmt1 = (insert(profile).
             values(id=1,
                    name="Ashlesha",
                    email="ashkharwale@gmail.com",
                    contact=7777777777)
             )

    stmt2 = (insert(profile).
             values(id=2,
                    name="Pradnya",
                    email="pradnyasonawane133@gmail.com",
                    contact=8888888888)
             )

    engine.execute(stmt1)
    engine.execute(stmt2)


def delete_profile(profile):
    engine, _ = get_connection()
    s = delete(profile)
    engine.execute(s)


if __name__ == "__main__":
    try:
        conn, meta_data = get_connection()
        print(conn)
        print(conn.table_names())

        profile_table = create_profile()
        insert_profile(profile_table)
        profile_data = select_profile(profile_table)
        print(profile_data)

    except Exception as ex:
        print("Could not complete execution due to the following error: \n", ex)


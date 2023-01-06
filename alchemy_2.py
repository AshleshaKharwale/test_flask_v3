"""
engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{db}")
"""
from sqlalchemy import create_engine, MetaData, Table, Column, INTEGER, VARCHAR, Numeric


# configurations of mysql
user = "root"
password = "Ash95kh"
host = "localhost"
db = "starwarsdb2"

# establishing connection
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")

# initializing MetaData() object
meta_data = MetaData(bind=engine)
MetaData.reflect(meta_data)

# creating table schema
books = Table(
    "books",
    meta_data,
    Column("book_id", INTEGER, primary_key=True),
    Column("name", VARCHAR(250)),
    Column("price", Numeric),
    Column("genre", VARCHAR(250))
)

# creating table in mysql database
meta_data.create_all(engine)

# insert records into the table
row1 = books.insert().values(book_id=1, name="Old age", price=12.2, genre="Fiction")
row2 = books.insert().values(book_id=2, name="Saturn Rings", price=13.2, genre="Non-fiction")
row3 = books.insert().values(book_id=3, name="Supernova", price=121.6, genre="Fiction")
row4 = books.insert().values(book_id=4, name="History of the world", price=100, genre="Non-fiction")
row5 = books.insert().values(book_id=5, name="Sun city", price=1112.2, genre="Fiction")

# execute the insert record statements
engine.execute(row1)
engine.execute(row2)
engine.execute(row3)
engine.execute(row4)
engine.execute(row5)

"""
DML stands for Data Manipulation Language

This module contains generic functions to insert data into sql tables
"""
from pymysql.err import IntegrityError
from models.dal.db_conn_helper import get_db_conn
from typing import Tuple, Dict


def insert_resource(
    table_name: str, data: Dict
):
    """
    Returns result of sql query execution.
    Inserts given data to the given table

    :param table_name: sql table name
    :param data: data in dictionary format
    :return: cursor output
    """
    sql_query = f"insert into {table_name} ({', '.join(data.keys())}) values {tuple(data.values())}"
    # breakpoint()
    # Generates query with table_name, dictionary keys as column names and
    # dictionary values as values.

    with get_db_conn() as conn:
        cursor = conn.cursor()
        try:
            result = cursor.execute(sql_query)
            conn.commit()
            return result
        except IntegrityError:
            return 0


def fetch_resources(table_name: str) -> Tuple:
    sql_query = f"select * from {table_name};"
    # breakpoint()
    with get_db_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
    return result


def fetch_resource(table_name: str, primary_key: str, primary_value: int) -> Tuple:
    sql_query = f"select * from {table_name} where {primary_key} = {primary_value};"

    with get_db_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchone()
    return result


def delete_resource(table_name: str, primary_key: str, primary_value: int) -> int:
    sql_query = f"delete from {table_name} where {primary_key}={primary_value};"

    with get_db_conn() as conn:
        cursor = conn.cursor()
        result = cursor.execute(sql_query)
        conn.commit()
    return result


def update_resource(table_name: str, data_set: Dict, primary_key: str, primary_value: int) -> int:
    breakpoint()
    sql_query = "update {} set {} where {}={};"
    set_values = []
    for key, value in data_set.items():
        if isinstance(value, int):
            val = f"{key}={value}"
            set_values.append(val)
        else:
            val = f"{key}='{value}'"
            set_values.append(val)

    set_values = ",".join(set_values)
    sql_query = sql_query.format(table_name, set_values, primary_key, primary_value)
    print(sql_query)


if __name__ == "__main__":
    data = {
        "film_id": 6,
        "title": "Revenge of the Sith",
        "episode_id": 3,
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": "2005-05-19",
        "created": "2014-12-20T18:49:38.403000Z",
        "edited": "2014-12-20T20:47:52.073000Z",
        "url": "https://swapi.dev/api/films/6/"
    }
    update_resource("film", data, "film_id", data.pop("film_id"))

#import mysql.connector
import sqlite3
import os


class DBHelper:
    def __init__(self, path_to_db: str = os.path.join("resource", "BaZaDaNyCh.db")) -> None:
        self.__conn = sqlite3.connect(path_to_db)
        self.__drop_table()
        self.__create_table()

    def __del__(self) -> None:
        self.__conn.close()

    def __drop_table(self) -> None:
        cur = self.__conn.cursor()
        drop_table = "DROP TABLE IF EXISTS `data_table`;"
        cur.execute(drop_table)
        self.__conn.commit()
        cur.close()

    def __create_table(self) -> None:
        cur = self.__conn.cursor()
        create_table = "CREATE TABLE IF NOT EXISTS `data_table` (Id integer PRIMARY KEY, Data LONGBLOB NOT NULL);"
        cur.execute(create_table)
        self.__conn.commit()
        cur.close()

    def insert_into_db(self, data: bytes) -> int:
        sql = f"INSERT INTO `data_table` (`Data`) VALUES (?);"
        cur = self.__conn.cursor()
        cur.execute(sql, (data,))
        self.__conn.commit()
        id_in_db = cur.lastrowid
        cur.close()
        return id_in_db

    def select_from_db(self, id: int) -> bytes:
        sql = f"SELECT `Data` FROM `data_table` WHERE Id = ?;"
        cur = self.__conn.cursor()
        cur.execute(sql, (id,))
        records = cur.fetchall()
        cur.close()
        return records[0][0]

import mysql.connector


class DBHelper:
    def __init__(
        self,
        host="127.0.0.1",
        user="qwerty",
        password="qwerty",
        database="datadb",
        use_unicode=False,
        charset="utf8",
    ):
        self.__conn = None
        try:
            self.__conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                use_unicode=use_unicode,
                charset=charset,
            )
        except Exception as e:
            print(f"Nie udało się połaczyć z bazą danych: {e}")
        self.drop_table()
        self.create_table()

    def __del__(self):
        self.__conn.close()

    def drop_table(self) -> None:
        cur = self.__conn.cursor()
        drop_table = "DROP TABLE IF EXISTS `data_table`;"
        cur.execute(drop_table)
        self.__conn.commit()
        cur.close()

    def create_table(self) -> None:
        cur = self.__conn.cursor()
        create_table = "CREATE TABLE `data_table` ( Id int NOT NULL AUTO_INCREMENT, Data LONGBLOB NOT NULL, PRIMARY KEY (Id));"
        cur.execute(create_table)
        self.__conn.commit()
        cur.close()

    def insert_into_db(self, data: bytes) -> int:
        sql = f"INSERT INTO `data_table` (`Data`) VALUES (%s);"
        cur = self.__conn.cursor()
        cur.execute(sql, (data,))
        self.__conn.commit()
        id_in_db = cur.lastrowid
        cur.close()
        return id_in_db

    def select_from_db(self, id: int) -> bytes:
        sql = f"SELECT `Data` FROM `data_table` WHERE Id = %s;"
        cur = self.__conn.cursor()
        cur.execute(sql, (id,))
        records = cur.fetchall()
        cur.close()
        return records[0][0]

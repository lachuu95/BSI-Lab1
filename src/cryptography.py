from Crypto.Cipher import AES
import pymysql


class Code:
    def __init__(self) -> None:
        self.__key = b"T%BLQyMMB*X+pCyM?Vj3ryvPeFws^5HE"


    def code(self, data: bytes) -> bytes:
        self.__cipher = AES.new(self.__key, AES.MODE_EAX)
        self.__nonce = self.__cipher.nonce
        ciphertext, self.__tag = self.__cipher.encrypt_and_digest(data)
        return ciphertext

    def decode(self, cipher_data: bytes) -> bytes:
        self.__cipher = AES.new(self.__key, AES.MODE_EAX, nonce=self.__nonce)
        data = self.__cipher.decrypt(cipher_data)
        try:
            print("The message is authentic")
            return data
        except ValueError:
            print("Key incorrect or message corrupted")

    def get_file_from_bytes(self, filename: str, data: bytes) -> None:
        f = open(filename, "wb")
        f.write(data)
        f.close

    def get_text_from_bytes(self, cipher_text: bytes) -> str:
        return cipher_text.decode()

    def get_bytes_from_file(self, filename: str) -> bytes:
        return open(filename, "rb").read()

    def get_bytes_from_text(self, text: str) -> bytes:
        return text.encode()

    def create_connection(
        self, host="127.0.0.1", user="qwerty", password="qwerty", database="datadb"
    ):
        conn = None
        print(host, user, password, database)
        try:
            conn = pymysql.connect(
                host=host, user=user, password=password, database=database
            )
            cur = conn.cursor()
            drop_table = "DROP TABLE data_table;"
            create_table = "CREATE TABLE data_table ( Id int NOT NULL AUTO_INCREMENT, Data LONGBLOB NOT NULL, PRIMARY KEY (Id));"
            cur.execute(drop_table)
            conn.commit()
            cur.execute(create_table)
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"nie udało się połaczyć z bazą danych {e}")
        return conn

    def insert_into_db(self, conn, data: bytes):
        sql = f"INSERT INTO `data_table` (`Data`) VALUES (%s);"
        cur = conn.cursor()
        cur.execute(sql, (data,))
        conn.commit()
        return cur.lastrowid


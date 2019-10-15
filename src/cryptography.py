from Crypto.Cipher import AES
import sqlite3


class Code:
    def __init__(self) -> None:
        self.__key = b"T%BLQyMMB*X+pCyM?Vj3ryvPeFws^5HE"
        self.__cipher = AES.new(self.__key, AES.MODE_EAX)
        self.__nonce = self.__cipher.nonce

    def code(self, data: bytes) -> bytes:
        ciphertext, self.__tag = self.__cipher.encrypt_and_digest(data)
        return ciphertext

    def decode(self, cipher_data: bytes) -> bytes:
        data = self.__cipher.decrypt(cipher_data)
        try:
            self.__cipher.verify(self.__tag)
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

    def create_connection(self, db_path:str):
        conn = None
        try:
            conn = sqlite3.connect(db_path)
        except:
            print("nie udało się połaczyć z bazą danych")
        return conn

    def insert_into_db(self, conn, data:bytes):
        #TODO: zmienić nazwę tabeli
        sql = f"INSERT INTO table_name VALUES ({data});"
        cur = conn.cursor()
        cur.execute(sql)
        return cur.lastrowid


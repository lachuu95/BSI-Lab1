from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class Code:
    def __init__(self, key:bytes=b"T%BLQyMMB*X+pCyM?Vj3ryvPeFws^5HE") -> None:
        self.__key = self.__validate_key(key)
        self.__nonce = get_random_bytes(8)

    def __validate_key(self, key):
        key_len = [16, 24, 32]
        if len(key) not in key_len:
            print(f"Klucz powinien mieć długość {key_len}")
            print(f"Obecna długość klucza: {len(key)}")
            key = get_random_bytes(32)
            print(f"klucz użyty do zaszyfrowania danych: {key}")
        return key

    def code(self, data: bytes) -> bytes:
        cipher = AES.new(self.__key, AES.MODE_CTR, nonce=self.__nonce)
        cipher_data = cipher.decrypt(data)
        return cipher_data

    def decode(self, cipher_data: bytes) -> bytes:
        try:
            cipher = AES.new(self.__key, AES.MODE_CTR, nonce=self.__nonce)
            data = cipher.decrypt(cipher_data)
            return data
        except ValueError as e:
            print(f"Klucz nie poprawny lub zepsuta wiadomość: {e}")

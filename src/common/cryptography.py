from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class Cryptography:
    def __init__(self, key: bytes = b"T%BLQyMMB*X+pCyM?Vj3ryvPeFws^5HE") -> None:
        self.__validate_key(key)
        self.__key = key
        self.__nonce = b""

    def __validate_key(self, key: bytes) -> None:
        key_len = [16, 24, 32]
        if len(key) not in key_len:
            raise ValueError(f"Klucz powinien mieć długość {key_len}, obecna długość klucza: {len(key)}")

    def code(self, data: bytes) -> bytes:
        cipher = AES.new(self.__key, AES.MODE_CTR, nonce=self.__nonce)
        cipher_data = cipher.decrypt(data)
        return cipher_data

    def decode(self, cipher_data: bytes) -> bytes:
        cipher = AES.new(self.__key, AES.MODE_CTR, nonce=self.__nonce)
        data = cipher.decrypt(cipher_data)
        return data

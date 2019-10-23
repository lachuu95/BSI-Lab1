from src.common.db_helper import DBHelper
from src.common.cryptography import Code


class CodeHelper:
    def __init__(self):
        self.__db_helper = DBHelper()
        self.__code = Code()

    def code_text_to_file(self, text: str, file_path_out: str) -> None:
        print(f"wejściowy tekst: {text}")
        text_bytes = text.encode()
        text_code = self.__code.code(text_bytes)
        with open(file_path_out, "wb") as file_object:
            file_object.write(text_code)

    def decode_file_to_text(self, file_path_out: str) -> str:
        with open(file_path_out, "rb") as file_object:
            text_code = file_object.read()
        print(f"zawarość wczytanego pliku: {text_code}")
        text_bytes = self.__code.decode(text_code)
        text_decode = text_bytes.decode()
        return text_decode

    def code_file_to_file(self, path_to_file: str, file_path_out_code: str) -> None:
        with open(path_to_file, "rb") as file_object:
            file_bytes = file_object.read()
        file_code = self.__code.code(file_bytes)
        with open(file_path_out_code, "wb") as file_object:
            file_object.write(file_code)

    def decode_file_to_file(
        self, file_path_out_code: str, file_path_out_decode: str
    ) -> None:
        with open(file_path_out_code, "rb") as file_object:
            file_code = file_object.read()
        file_decode = self.__code.decode(file_code)
        with open(file_path_out_decode, "wb") as file_object:
            file_object.write(file_decode)

    def code_file_to_db(self, path_to_file: str) -> int:
        with open(path_to_file, "rb") as file_object:
            file_bytes = file_object.read()
        file_code = self.__code.code(file_bytes)
        file_id = self.__db_helper.insert_into_db(file_code)
        return file_id

    def decode_db_to_file(self, file_id: int, file_path_out_decode: str) -> None:
        file_code = self.__db_helper.select_from_db(file_id)
        file_decode = self.__code.decode(file_code)
        with open(file_path_out_decode, "wb") as file_object:
            file_object.write(file_decode)

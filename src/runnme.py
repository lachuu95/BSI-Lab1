#!./.env/bin/python
from cryptography import Code
import os


def code_text(code):
    text = input("Wpisz tekst do zakodowania: ")
    text_bytes = code.get_bytes_from_text(text)
    print(f"wejściowy tekst: {text}")
    return code.code(text_bytes)


def decode_text(text_code:bytes, code):
    print(f"Zakodowany tekst: {text_code}")
    text_decode = code.decode(text_code)
    print(f"zdekodowany tekst: {code.get_text_from_bytes(text_decode)}")


def code_file(code):
    file_path = input("Wpisz ścieżke do pliku do zakodowania: ")
    if not os.path.exists(file_path):
        print("podany plik nie istnieje!!!")
        file_path = "resource/docker-compose.yml"
    file_ext = os.path.splitext(file_path)[1]
    file_bytes = code.get_bytes_from_file(file_path)
    print(f"wejściowy plik: {file_path}")
    return (code.code(file_bytes), file_ext)


def decode_file(file_data, code):
    file_code, file_ext = file_data
    print(f"zakodowany plik: {file_code}")
    file_decode = code.decode(file_code)
    code.get_file_from_bytes(f"odkodowanyPlik{file_ext}", file_decode)
    print(f"zdekodowany plik: odkodowanyPlik{file_ext}")


def code_to_db(code):
    conn = code.create_connection()
    text_code = code_text(code)
    print(code.insert_into_db(conn, text_code))
    file_code, _ = code_file(code)
    print(code.insert_into_db(conn, file_code))
    conn.close()


def main():

    code = Code()

    temp = code_text(code)
    decode_text(temp, code)

    temp = code_file(code)
    decode_file(temp, code)

    code_to_db(code)


if __name__ == "__main__":
    main()

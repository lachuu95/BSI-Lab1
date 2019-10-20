#!./.env/bin/python
from cryptography import Code
import os


def code_text(code):
    # text = input("Wpisz tekst do zakodowania: ")
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    text_bytes = code.get_bytes_from_text(text)
    print(f"wejściowy tekst: {text}")
    return code.code(text_bytes)


def decode_text(text_code: bytes, code):
    print(f"Zakodowany tekst: {text_code}")
    text_decode = code.decode(text_code)
    print(f"zdekodowany tekst: {code.get_text_from_bytes(text_decode)}")


def code_file(code):
    # file_path = input("Wpisz ścieżke do pliku do zakodowania: ")
    file_path = "resource/image.jpg"
    file_ext = os.path.splitext(file_path)[1]
    file_bytes = code.get_bytes_from_file(file_path)
    print(f"wejściowy plik: {file_path}")
    return (code.code(file_bytes), file_ext)


def decode_file(file_data, code):
    file_code, file_ext = file_data
    print(f"zakodowany plik: {file_code[:10]}...")
    file_decode = code.decode(file_code)
    code.get_file_from_bytes(f"odkodowanyPlik{file_ext}", file_decode)
    print(f"zdekodowany plik: odkodowanyPlik{file_ext}")


def code_text_to_db(code, conn):
    text_code = code_text(code)
    return code.insert_into_db(conn, text_code)


def decode_text_from_db(id, code, conn):
    text_code = code.select_from_db(conn, id)
    decode_text(text_code, code)


def code_file_to_db(code, conn):
    file_code, file_ext  = code_file(code)
    return (code.insert_into_db(conn, file_code), file_ext)


def decode_file_from_db(file_data, code, conn):
    file_id, file_ext = file_data
    file_code = (code.select_from_db(conn, file_id), file_ext)
    decode_file(file_code, code)


def main():

    code = Code()

    temp = code_text(code)
    decode_text(temp, code)

    temp = code_file(code)
    decode_file(temp, code)

    conn = code.create_connection()
    temp = code_text_to_db(code, conn)
    decode_text_from_db(temp, code, conn)

    temp = code_file_to_db(code, conn)
    decode_file_from_db(temp, code, conn)
    conn.close()


if __name__ == "__main__":
    main()

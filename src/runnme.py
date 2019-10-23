#!/usr/bin/env python3

import os
import argparse
from cryptography import Code
from db_helper import DBHelper


def main(text, path_to_file):

    code = Code()

    file_path_out = "resource/text_code_file"
    print(f"wejściowy tekst: {text}")
    text_bytes = text.encode()
    text_code = code.code(text_bytes)
    print(text_code)
    with open(file_path_out, "wb") as file_object:
        file_object.write(text_code)

    with open(file_path_out, "rb") as file_object:
        text_code = file_object.read()
    text_bytes = code.decode(text_code)
    text_decode = text_bytes.decode()
    print(f"wyjściowy tekst: {text_decode}")

    file_path_out_code = "resource/file_code_file"
    file_ext = os.path.splitext(path_to_file)[1]
    file_path_out_decode = f"resource/file_decode_file{file_ext}"
    with open(path_to_file, "rb") as file_object:
        file_bytes = file_object.read()
    file_code = code.code(file_bytes)
    with open(file_path_out_code, "wb") as file_object:
        file_object.write(file_code)

    with open(file_path_out_code, "rb") as file_object:
        file_code = file_object.read()
    file_decode = code.decode(file_code)
    with open(file_path_out_decode, "wb") as file_object:
        file_object.write(file_decode)

    db_helper = DBHelper()
    file_ext = os.path.splitext(path_to_file)[1]
    file_path_out_decode = f"resource/db_decode_file{file_ext}"
    with open(path_to_file, "rb") as file_object:
        file_bytes = file_object.read()
    file_code = code.code(file_bytes)
    file_id = db_helper.insert_into_db(file_code)

    file_code = db_helper.select_from_db(file_id)
    file_decode = code.decode(file_code)
    with open(file_path_out_decode, "wb") as file_object:
        file_object.write(file_decode)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Code and decode text, file, file with db."
    )
    parser.add_argument("text", type=str, help="Text to code and decode.")
    parser.add_argument("path_to_file", type=str, help="Path file to code and decode")
    args = parser.parse_args()
    if os.path.isfile(args.path_to_file):
        main(args.text, args.path_to_file)
    else:
        print(f"File {args.path_to_file} doesn't exist.")

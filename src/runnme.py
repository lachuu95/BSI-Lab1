#!/usr/bin/env python3

import os
import argparse
from code_helper import CodeHelper


def main(text: str, path_file_input: str) -> None:

    code_helper = CodeHelper()
    file_input_ext = os.path.splitext(path_file_input)[1]
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    path_file_code = f"{output_dir}/text_code_file"
    code_helper.code_text_to_file(text, path_file_code)

    text_decode = code_helper.decode_file_to_text(path_file_code)
    print(f"wyjściowy tekst: {text_decode}")

    path_file_code = f"{output_dir}/file_code_file"
    code_helper.code_file_to_file(path_file_input, path_file_code)

    path_file_output = f"{output_dir}/file_decode_file{file_input_ext}"
    code_helper.decode_file_to_file(path_file_code, path_file_output)

    file_id = code_helper.code_file_to_db(path_file_input)

    path_file_output = f"{output_dir}//db_decode_file{file_input_ext}"
    code_helper.decode_db_to_file(file_id, path_file_output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Kodowanie i dekodowanie tekstu, pliku i pliku z zapisem do bazy danych."
    )
    parser.add_argument("text", type=str, help="Tekst do zakodowania.")
    parser.add_argument("path_to_file", type=str, help="Ścierzka pliku do zakodowania.")
    args = parser.parse_args()
    if os.path.isfile(args.path_to_file):
        main(args.text, args.path_to_file)
    else:
        print(f"Plik o ścierzce: {args.path_to_file} nie istnieje.")

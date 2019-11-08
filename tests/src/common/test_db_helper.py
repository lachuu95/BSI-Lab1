import pytest
import sys
import os

sys.path.append(os.path.abspath("."))
from src.common.db_helper import DBHelper


def test_DBHelper(tmpdir):
    db_path = tmpdir.join("hello.db")
    DBHelper(db_path)
    assert True
    # sprawdz czy plik istnieje
    # sprawdz czy tabela w pliku istnieje

# mockowanie dla wszystkich xd

# sprawdz czy wstawia do tabeli

# sprawdz czy odczytuje z tablei
import pytest
import sys
import os

sys.path.append(os.path.abspath("."))
from src.common.db_helper import DBHelper


def test_DBHelper(tmpdir):
    db_path = tmpdir.join("hello.db")
    DBHelper(db_path)
    assert True
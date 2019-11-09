import pytest
import sqlite3
import mock
import sys
import os

sys.path.append(os.path.abspath("."))
from src.common.db_helper import DBHelper


@mock.patch("src.common.db_helper.sqlite3")
def test_DBHelper(mock_sqlite3):
    mocked_cursor = mock.MagicMock(sqlite3.Cursor)
    mocked_connect = mock.MagicMock(sqlite3.Connection)
    mocked_connect.cursor.return_value = mocked_cursor
    mock_sqlite3.connect.return_value = mocked_connect

    DBHelper()

    assert mock_sqlite3.connect.call_count == 1
    mock_sqlite3.connect.assert_called_with(os.path.join("resource", "BaZaDaNyCh.db"))
    assert mocked_connect.cursor.call_count == 2
    assert mocked_connect.commit.call_count == 2
    assert mocked_cursor.execute.call_count == 2
    mocked_cursor.execute.assert_has_calls(
        [
            mock.call("DROP TABLE IF EXISTS `data_table`;"),
            mock.call(
                "CREATE TABLE IF NOT EXISTS `data_table` (Id integer PRIMARY KEY, Data LONGBLOB NOT NULL);"
            ),
        ]
    )
    assert mocked_cursor.close.call_count == 2


@mock.patch("src.common.db_helper.sqlite3")
def test_insert_into_db(mock_sqlite3):
    mocked_cursor = mock.MagicMock(sqlite3.Cursor)
    type(mocked_cursor).lastrowid = mock.PropertyMock(return_value=1)
    mocked_connect = mock.MagicMock(sqlite3.Connection)
    mocked_connect.cursor.return_value = mocked_cursor
    mock_sqlite3.connect.return_value = mocked_connect

    db_helper = DBHelper()
    id_in_db = db_helper.insert_into_db(b"test")

    assert mocked_connect.cursor.call_count == 3
    assert mocked_connect.commit.call_count == 3
    assert mocked_cursor.execute.call_count == 3
    mocked_cursor.execute.assert_called_with(
        "INSERT INTO `data_table` (`Data`) VALUES (?);", (b"test",)
    )
    assert mocked_cursor.close.call_count == 3
    assert id_in_db == 1


@mock.patch("src.common.db_helper.sqlite3")
def test_select_from_db(mock_sqlite3):
    mocked_cursor = mock.MagicMock(sqlite3.Cursor)
    mocked_cursor.fetchall.return_value = [
        (b"test",),
    ]
    mocked_connect = mock.MagicMock(sqlite3.Connection)
    mocked_connect.cursor.return_value = mocked_cursor
    mock_sqlite3.connect.return_value = mocked_connect

    db_helper = DBHelper()
    value = db_helper.select_from_db(1)

    assert mocked_connect.cursor.call_count == 3
    assert mocked_connect.commit.call_count == 2
    assert mocked_cursor.execute.call_count == 3
    mocked_cursor.execute.assert_called_with(
        "SELECT `Data` FROM `data_table` WHERE Id = ?;", (1,)
    )
    assert mocked_cursor.close.call_count == 3
    assert value == b"test"

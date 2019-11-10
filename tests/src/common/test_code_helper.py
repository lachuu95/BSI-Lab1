import pytest
import mock
import sys
import os

sys.path.append(os.path.abspath("."))
from src.common.code_helper import CodeHelper
from src.common.db_helper import DBHelper
from src.common.cryptography import Cryptography


@mock.patch("src.common.code_helper.Cryptography")
@mock.patch("src.common.code_helper.DBHelper")
def test_codehelper(mock_db_helper, mock_cryptography):
    CodeHelper()
    assert mock_cryptography.call_count == 1
    assert mock_db_helper.call_count == 1
    

@mock.patch("src.common.code_helper.Cryptography")
@mock.patch("src.common.code_helper.DBHelper")
def test_code_text_to_file(mock_db_helper, mock_cryptography, tmp_path):
    mocked_cryptography = mock.MagicMock(Cryptography)
    mocked_cryptography.code.return_value = b"test"
    mock_cryptography.return_value = mocked_cryptography
    file_path = tmp_path / "test"

    code_helper = CodeHelper()
    code_helper.code_text_to_file("test", file_path)

    assert file_path.read_text() == "test"
    mocked_cryptography.code.assert_called_with(b"test")

@mock.patch("src.common.code_helper.Cryptography")
@mock.patch("src.common.code_helper.DBHelper")
def test_decode_file_to_text(mock_db_helper, mock_cryptography, tmp_path):
    mocked_cryptography = mock.MagicMock(Cryptography)
    mocked_cryptography.decode.return_value = b"test"
    mock_cryptography.return_value = mocked_cryptography
    file_path = tmp_path / "test"
    file_path.write_text("test")
    assert file_path.read_text() == "test"

    code_helper = CodeHelper()
    value = code_helper.decode_file_to_text(file_path)

    assert value == "test"
    mocked_cryptography.decode.assert_called_with(b"test")


@mock.patch("src.common.code_helper.Cryptography")
@mock.patch("src.common.code_helper.DBHelper")
def test_code_file_to_file(mock_db_helper, mock_cryptography, tmp_path):
    mocked_cryptography = mock.MagicMock(Cryptography)
    mocked_cryptography.code.return_value = b"test"
    mock_cryptography.return_value = mocked_cryptography
    file_path_in = tmp_path / "test.txt"
    file_path_in.write_text("test")
    file_path_out = tmp_path / "test"
    assert file_path_in.read_text() == "test"

    code_helper = CodeHelper()
    code_helper.code_file_to_file(file_path_in, file_path_out)

    assert file_path_out.read_text() == "test"
    mocked_cryptography.code.assert_called_with(b"test")


@mock.patch("src.common.code_helper.Cryptography")
@mock.patch("src.common.code_helper.DBHelper")
def test_decode_file_to_file(mock_db_helper, mock_cryptography, tmp_path):
    mocked_cryptography = mock.MagicMock(Cryptography)
    mocked_cryptography.decode.return_value = b"test"
    mock_cryptography.return_value = mocked_cryptography
    file_path_in = tmp_path / "test"
    file_path_in.write_text("test")
    file_path_out = tmp_path / "test.txt"
    assert file_path_in.read_text() == "test"

    code_helper = CodeHelper()
    code_helper.decode_file_to_file(file_path_in, file_path_out)

    assert file_path_out.read_text() == "test"
    mocked_cryptography.decode.assert_called_with(b"test")


@mock.patch("src.common.code_helper.Cryptography")
@mock.patch("src.common.code_helper.DBHelper")
def test_code_file_to_db(mock_db_helper, mock_cryptography, tmp_path):
    mocked_cryptography = mock.MagicMock(Cryptography)
    mocked_cryptography.code.return_value = b"test"
    mocked_db_helper = mock.MagicMock(DBHelper)
    mocked_db_helper.insert_into_db.return_value = 1
    mock_cryptography.return_value = mocked_cryptography
    mock_db_helper.return_value = mocked_db_helper
    file_path = tmp_path / "test.txt"
    file_path.write_text("test")
    assert file_path.read_text() == "test"

    code_helper = CodeHelper()
    id_in_db = code_helper.code_file_to_db(file_path)

    mocked_cryptography.code.assert_called_with(b"test")
    mocked_db_helper.insert_into_db.assert_called_with(b"test")
    assert id_in_db == 1



@mock.patch("src.common.code_helper.Cryptography")
@mock.patch("src.common.code_helper.DBHelper")
def test_decode_db_to_file(mock_db_helper, mock_cryptography, tmp_path):
    mocked_cryptography = mock.MagicMock(Cryptography)
    mocked_cryptography.decode.return_value = b"test"
    mocked_db_helper = mock.MagicMock(DBHelper)
    mocked_db_helper.select_from_db.return_value = b"test"
    mock_cryptography.return_value = mocked_cryptography
    mock_db_helper.return_value = mocked_db_helper
    file_path = tmp_path / "test.txt"

    code_helper = CodeHelper()
    code_helper.decode_db_to_file(1, file_path)

    mocked_cryptography.decode.assert_called_with(b"test")
    mocked_db_helper.select_from_db.assert_called_with(1)
    assert file_path.read_text() == "test"
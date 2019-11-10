import pytest
import sys
import os

sys.path.append(os.path.abspath("."))
from src.common.cryptography import Cryptography

def test_Cryptography():
    Cryptography()
    assert True

@pytest.mark.parametrize("test_input_key", [b"QQk8!4DA@6TJuV!y", b"2Wuua+Yj+$Wc?D59wAA^wDz#", b"7%9w^gk32Js#sWK#qWhj424!Wk@SHxLj"])
def test_Cryptography_with_key(test_input_key):
    Cryptography(test_input_key)
    assert True

@pytest.mark.parametrize("test_input_key", [b"", b"test", b"JWCd#L#38^"])
def test_Cryptography_with_wrong_key(test_input_key):
    with pytest.raises(ValueError):
        Cryptography(test_input_key)

@pytest.fixture(scope="module")
def get_class_object():
    yield Cryptography()

def test_code(get_class_object):
    assert get_class_object.code(b"test") == b"\x81\xd2\xfb\xc0"

def test_decode(get_class_object):
    assert get_class_object.decode(b"\x81\xd2\xfb\xc0") == b"test"

def test_decode_with_wrong_key():
    code = Cryptography(b"QQk8!4DA@6TJuV!y")
    assert code.decode(b"\x81\xd2\xfb\xc0") != b"test"
# Dinu - version 3 - added more tests, postitive validation and negativ validation

import pytest
from verify import validate_username

@pytest.mark.parametrize("username", [
    "John123", "A1B2C3", "Zoe", "Bob007"
])
def test_valid_usernames(username):
    assert validate_username(username) == True

@pytest.mark.parametrize("username", [
    "123John", "_username", "user!", "", " ", "john doe", "A@B"
])
def test_invalid_usernames(username):
    assert validate_username(username) == False

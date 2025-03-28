from verify import validate_username

def test_valid_usernames():
    assert validate_username("John123") == True
    assert validate_username("Alice007") == True

def test_invalid_usernames():
    assert validate_username("123John") == False
    assert validate_username("john_doe") == False
    assert validate_username("!badname") == False
    assert validate_username("John*") == False

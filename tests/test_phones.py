import pytest
import project1
from project1 import main
def test_phones():
    phone_test = "phone numbers: 854-235-6526"
    test = main.redact_phone_numbers(phone_test)
    assert test is not None

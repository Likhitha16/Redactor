import pytest
import project1
from project1 import main

def test_redactaddress():
    address_text = "1234 Main Street, Anytown, CA 12345"
    test = main.redact_address(address_text)
    assert test is not None



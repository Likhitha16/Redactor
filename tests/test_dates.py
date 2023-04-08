import pytest
import main
from project1 import main
def test_redact_dates():
    text_date = "01-12-1992 is my date of birth and my age is 26. He was born on 07 june 2000"    
    test = main.redact_dates(text_date)
    assert test is not None

import pytest
import project1
from project1 import main

def test_redact_genders():
    gender_text = "he visits my home always. he also visits his  dad and mom"
    test = main.redact_genders(gender_text)
    assert test is not None

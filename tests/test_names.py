import pytest
import glob
from project1 import main


def test_redact_names():
    text = "Tom is my name. Bob is my friend"
    test = main.redact_names(text)
    assert test is not None



import pytest
import os
import numpy

@pytest.mark.it('You should print the expected output')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == 'nan\nFalse\nFalse\nnan\nTrue\nFalse\n'

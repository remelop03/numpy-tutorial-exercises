import pytest
import os, re

@pytest.mark.it("Use the arange() function")
def test_output():
    f = open('app.py')
    content = f.read()
    assert content.find("arange(") > 0

@pytest.mark.it('The output should be a vector with all the integers from 10 to 49')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert '[10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33\n 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]\n' in captured.out

@pytest.mark.it("You should not be hard-coding the expected value")
def test_hard_code():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\[10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33\\n 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49\]\\n")
        assert bool(regex.search(content)) == False
import pytest
import os,re

@pytest.mark.it("Use the arange() function")
def test_arange_exists():
    f = open('app.py')
    content = f.read()
    assert content.find("arange(") > 0

@pytest.mark.it("You have to reverse the vector values")
def test_output():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\s*\:\s*\:\s*\-\s*1\s*")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The output should be a vector with all the integers from 9 to 0 inclusive of both ends')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert  '[9 8 7 6 5 4 3 2 1 0]\n' in captured.out

@pytest.mark.it("You should not be hard-coding the expected value")
def test_hard_code():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\[9 8 7 6 5 4 3 2 1 0\]\\n")
        assert bool(regex.search(content)) == False
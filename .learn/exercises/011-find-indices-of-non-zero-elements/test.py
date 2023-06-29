import pytest
import os, re

@pytest.mark.it("You have to use the nonzero() method")
def test_output():
    f = open('app.py')
    content = f.read()
    assert "nonzero" in content

@pytest.mark.it("You have to use the array() method")
def test_array_exists():
    f = open('app.py')
    content = f.read()
    assert "array" in content

@pytest.mark.it('The output should be a tuple of arrays with the indices of non zero values')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert   '(array([0, 1, 4]),)\n' in captured.out

@pytest.mark.it("You should not be hard-coding the expected value")
def test_hard_code():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\(array\(\[0, 1, 4\]\),\)")
        assert bool(regex.search(content)) == False
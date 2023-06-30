import pytest
import os,re

@pytest.mark.it("You have to use the eye() method")
def test_output():
    f = open('app.py')
    content = f.read()
    assert "eye(" in content

@pytest.mark.it('The output should be a matrix which values should be from 0 to 9')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert   '[[1. 0. 0.]\n [0. 1. 0.]\n [0. 0. 1.]]\n' in captured.out

@pytest.mark.it("You should not be hard-coding the expected value")
def test_hard_code():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\[\[1\. 0\. 0\.]\\n \[0\. 1\. 0\.]\\n \[0\. 0\. 1\.\]\]")
        assert bool(regex.search(content)) == False
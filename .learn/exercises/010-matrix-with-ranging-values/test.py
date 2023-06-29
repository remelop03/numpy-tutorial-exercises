import pytest
import os,re 

@pytest.mark.it("You have to use the reshape() method")
def test_output():
    f = open('app.py')
    content = f.read()
    assert content.find("reshape(") > 0

@pytest.mark.it('The output should be a matrix which values should be from 0 to 8')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert  '[[0 1 2]\n [3 4 5]\n [6 7 8]]\n' in captured.out

@pytest.mark.it("You should not be hard-coding the expected value")
def test_hard_code():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\[\[0 1 2\]\\n \[3 4 5\]\\n \[6 7 8\]\]\\n")
        assert bool(regex.search(content)) == False
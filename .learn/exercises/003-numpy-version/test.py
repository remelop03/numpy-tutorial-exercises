import os, pytest, re
import numpy as np

@pytest.mark.it("Import NumPy as np on the app.py file")
def test_declare_variable():
    path = 'app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import\s+numpy\s+as\s+np")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You have to access to the __version__ property")
def test_declare_variable():
    path = 'app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"np\s*\.\s*__version__")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The output should be the version 1.24.2')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert np.__version__ in captured.out

import pytest
import os,re
import numpy

@pytest.mark.it("You have to use the random() method")
def test_random():
    path = os.path.dirname(os.path.abspath('app.py'))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\s*random\s*\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('You should create a variable named arr')
def test_arr_exists():
    try:
        from app import arr
    except AttributeError:
        raise AttributeError("The variable 'arr' should exist on app.py")

@pytest.mark.it('The array should have three random values')
def test_arr_value(capsys):
    from app import arr
    size = numpy.size(arr)
    assert size == 3
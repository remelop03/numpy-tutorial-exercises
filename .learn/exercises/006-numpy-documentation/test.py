import pytest
import os, sys
import numpy 


@pytest.mark.it("You have to use the info() function")
def test_output():
    f = open('app.py')
    content = f.read()
    assert content.find("info(") > 0

@pytest.mark.it("You should be getting the documentation of np.add()")
def test_using_add(capsys, app):
    f = open('app.py')
    content = f.read()

    assert content.find("add") > 0

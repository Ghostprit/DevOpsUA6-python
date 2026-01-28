import pytest
from task1 import stringToList

@pytest.fixture
def strInput():
    return '4th generation jet fighter'
def testSplitting(strInput):
    assert stringToList(strInput) == ['4th', 'generation', 'jet', 'fighter']
def testEmptyString():
    assert stringToList('') == []
def testIfInt():
    with pytest.raises(TypeError):
        stringToList(1)

if __name__ == "__main__":
    pytest.main()
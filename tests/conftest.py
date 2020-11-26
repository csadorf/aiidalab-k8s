import pytest

@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(600) # seconds
    return selenium

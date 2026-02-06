import pytest
import uuid


@pytest.fixture
def first_name():
    return str(uuid.uuid4())
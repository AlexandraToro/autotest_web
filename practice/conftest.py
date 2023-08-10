import pytest


@pytest.fixture
def title():
	return "New post"


@pytest.fixture
def description():
	return "New description"


@pytest.fixture
def content():
	return "New content"

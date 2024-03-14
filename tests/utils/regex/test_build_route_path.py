import pytest
from src.utils.regex.build_route_path import build_route_path


@pytest.fixture
def path_regex():
    return build_route_path("/user/:userId/details/:detailId")


def test_build_route_path(path_regex):
    match = path_regex.match("/user/123/details/detail-456")
    assert match is not None
    assert match.group("userId") == "123"
    assert match.group("detailId") == "detail-456"


def test_build_route_path_with_query(path_regex):
    match = path_regex.match("/user/123/details/detail-456?query=test")
    assert match is not None
    assert match.group("query") == "?query=test"


def test_build_route_path_no_match(path_regex):
    match = path_regex.match("/invalid/123")
    assert match is None


def test_build_route_path_empty():
    with pytest.raises(ValueError) as excinfo:
        build_route_path(" ")
    assert str(excinfo.value) == "Invalid path"
    
    with pytest.raises(ValueError) as excinfo:
        build_route_path("")
    assert str(excinfo.value) == "Invalid path"

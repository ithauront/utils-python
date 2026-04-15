from src.utils.trim_to_last_word import trim_to_last_word_with_index


def test_removes_last_word():
    assert trim_to_last_word_with_index("hello world") == ("hello", 5)


def test_trailing_spaces():
    assert trim_to_last_word_with_index("hello world   ") == ("hello", 5)


def test_single_word():
    assert trim_to_last_word_with_index("hello") == ("hello", 5)


def test_only_spaces():
    assert trim_to_last_word_with_index("   ") == ("", 0)


def test_empty_string():
    assert trim_to_last_word_with_index("") == ("", 0)


def test_multiple_words():
    assert trim_to_last_word_with_index("one two three") == ("one two", 7)


def test_multiple_spaces_between_words():
    assert trim_to_last_word_with_index("one   two   three") == ("one   two", 11)

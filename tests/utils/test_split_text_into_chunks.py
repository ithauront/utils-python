from src.utils.split_text_into_chunks import split_text_into_chunks


def test_basic_split():
    text = "hello world this is a test"
    result = split_text_into_chunks(text, 10)

    assert result == ["hello", "world this", "is a test"]


def test_no_split_needed():
    text = "short text"
    result = split_text_into_chunks(text, 50)

    assert result == ["short text"]


def test_exact_length():
    text = "hello world"
    result = split_text_into_chunks(text, len(text))

    assert result == ["hello world"]


def test_trailing_spaces():
    text = "hello world   "
    result = split_text_into_chunks(text, 10)

    assert result == ["hello", "world"]


def test_single_long_word():
    text = "supercalifragilisticexpialidocious"
    result = split_text_into_chunks(text, 10)

    assert result == [
        "supercalif",
        "ragilistic",
        "expialidoc",
        "ious",
    ]

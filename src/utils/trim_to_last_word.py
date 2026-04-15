def trim_to_last_word_with_index(text: str) -> tuple[str, int]:
    """Trim text to the last complete word and return str and the index where the cut happend.

    Useful when splitting a long string into chunks with a maximum length.
    This ensures that words are not broken across chunks by removing the
    last (possibly incomplete) word from the current segment.
    """
    trimmed = text.rstrip()

    last_space_index = trimmed.rfind(" ")

    if last_space_index == -1:
        return trimmed, len(trimmed)

    return trimmed[:last_space_index].rstrip(), last_space_index

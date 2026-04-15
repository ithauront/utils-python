from src.utils.trim_to_last_word import trim_to_last_word_with_index


def split_text_into_chunks(text: str, max_length: int) -> list[str]:
    """Split text into chunks without breaking words.

    Given a string and a maximum chunk length, this function splits the text
    into multiple chunks ensuring that no word is split between two chunks.

    If a chunk would end in the middle of a word, the incomplete word is removed
    and pushed to the next chunk.
    """
    chunks = []

    while text:
        text = text.strip()

        if len(text) <= max_length:
            chunks.append(text)
            break

        window = text[:max_length]

        if len(text) > max_length and text[max_length : max_length + 1] == " ":
            chunks.append(window.strip())
            text = text[max_length:]
            continue

        chunk, cut_index = trim_to_last_word_with_index(window)

        chunks.append(chunk.strip())

        text = text[cut_index:].lstrip()

    return chunks

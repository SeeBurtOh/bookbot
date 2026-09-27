def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_chars_dict(text: str) -> dict[str, int]:
    chars={}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d: tuple[str, int]) -> int:
    return d[1]

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append((ch, chars_dict[ch]))
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list

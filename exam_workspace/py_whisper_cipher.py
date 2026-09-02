def whisper_cipher(text: str, shift: int) -> str:
    abc = "abcdefghijklmnopqrstuvwxyz"
    shift = shift % 26
    shifted_abc = abc[shift:] + abc[:shift]

    upper_abc = abc.upper()
    alphabet = abc + upper_abc

    shifted_ABC = shifted_abc.upper()
    target = shifted_abc + shifted_ABC

    return "".join(
        target[alphabet.index(c)] if c in alphabet else c for c in text)


# print(whisper_cipher("hedddddllo", 3))
# print(whisper_cipher("Hello World!", 1))
# print(whisper_cipher("xyz", 3))
# print(whisper_cipher("ABC123def", 5))
# print(whisper_cipher("", 10))
# print(whisper_cipher("abc", -3))

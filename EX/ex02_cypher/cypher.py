"""Caesari_siffer."""


def encode(message: str, key: int):
    """Encode."""
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message = message.lower()
    for letter in message:
        if letter in alphabet:
            position_in_alphabet = alphabet.find(letter)
            second_position = position_in_alphabet + key
            second_position = second_position % 26
            result = result + alphabet[second_position]

        else:
            result = result + letter
    return result


if __name__ == '__main__':
    print(encode("cat", 2))

"""Caesari_siffer."""


def encode(message: str, key: int):
    """Encode."""
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    message = message.lower()
    # if message in alphabet:
    for letter in message:
        position_in_alphabet = alphabet.find(letter)
        second_position = position_in_alphabet + key
        if letter in alphabet:
            result = result + alphabet[second_position]
        else:
            result = result + letter
    return result


if __name__ == '__main__':
    print("CAT", 2)

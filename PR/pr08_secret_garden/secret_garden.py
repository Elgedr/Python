"""Secret Garden."""

import base64


class Decoder:
    """Decoder class."""

    def __init__(self, file: str, key: str):
        """Decoder constructor."""
        self.file = file
        self.key = key

    def read_code_from_file(self) -> list:
        """Read file lines to a list."""
        res = []
        with open(self.file, encoding='utf-8') as f:
            for line in f:
                res.append(line.strip('\n'))
        return res

    @staticmethod  # метод, который можно вызывать используя .
    def decode_from_base64(data: str) -> str:
        """Decode base64 string to utf-8 string."""
        message = data
        first = message.encode("UTF-8")
        second = base64.b64encode(first)
        third = second.decode('UTF-8')
        fourth = third.encode('UTF-8')
        fifth = base64.b64decode(fourth)
        sixth = fifth.decode('UTF-8')
        return sixth

    def calculate_cipher_step(self) -> int:
        """Calculate cipher step."""
        res = []
        for letter in self.key:
            res.append(ord(letter))  # ord метод возвращает число, представляющее 1 символ (юникода) из строки
        return sum(res)

    def decode(self) -> list:
        """"""




class SecretGarden:
    """SecretGarden class."""

    def __init__(self, file: str, key: str):
        """"""
        self.file = file
        self.key = key

    def decode_messages(self) -> list:
        """"""

    def find_secret_locations(self) -> list:
        """"""


if __name__ == '__main__':
    d = Decoder('pr08_example_data.txt', 'Fat Chocobo')
    print(d.read_code_from_file())  # ['KS0uNyktBgZBT08=', ...]
    print(d.decode_from_base64('MDsyCgpOTlNXV0U='))  # 0;2\n\nNNSWWE
    print(d.calculate_cipher_step())  # 70 + 97 + 116 + 32 + ... -> 1016
    print(d.decode())  # ['-12;-1\n\nESS', ...]

    sg = SecretGarden('pr08_example_data.txt', 'Fat Chocobo')
    print(sg.decode_messages())  # ['-12;-1\n\nESS', ...]
    print(sg.find_secret_locations())  # [(-11, -3), (20, -13), (1, -3), (-2, -5), (10, 4), (6, -13), (2, -6)]
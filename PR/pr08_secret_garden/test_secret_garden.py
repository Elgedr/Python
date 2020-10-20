import pytest

from secret_garden import Decoder, SecretGarden  # из файла импортируем классы

filename = 'pr08_example_data.txt'
key = 'Fat Chocobo'
# сюда пишем все переменные которые вводятся в конструктор класса


def test_decode():  # все функции в тестере должны начинаться со слова test. Название говорит о том,
    # какую функцию мы тестерим
    """Funktsioon."""
    d = Decoder(filename, key)

    assert len(d.decode()) == 7
    assert d.decode()[0] == '-12;-1\n\nESS'  # после . пишем функцию из класса, которую проверяем
    assert d.decode()[1] == '19;-14\n\nNEWNESSEWN'
    # слева наш результат - справа тот, который должен получиться
    assert d.read_code_from_file()[0] == 'KS0uNyktBgZBT08='
    assert d.decode_from_base64('MDsyCgpOTlNXV0U=') == '0;2\n\nNNSWWE'
    assert d.calculate_cipher_step() == 1016


def test_secretgarden():
    """Funktsioon."""
    sg = SecretGarden(filename, key)

    assert sg.decode_messages()[0] == '-12;-1\n\nESS'
    assert len(sg.find_secret_locations()) == 7

"""Book_sortation."""


def add_book_to_category(book: str, category: str, categorised_books: dict):
    """1 funktsioon."""
    categorised_books = {"spell books": [""], "history books": [""], "relics books": [""], "potion books": [""], "other books": [""]}
    # if book in
    # return dict


def is_spell_book(book: str) -> bool:
    """2 funktsioon."""
    if book.startswith("*") and book.endswith("*"):
        return True
    return False


def is_history_book(book: str) -> bool:
    """3 funktsioon."""
    if book == book.title():
        return True
    return False


def is_relics_book(book: str) -> bool:
    """4 funktsioon."""
    if book[0::2].islower() and book[1::2].isupper() or book[0::2].isupper() and book[1::2].islower():
        return True
    return False


def is_potion_book(book: str) -> bool:
    """5 funktsioon."""
    taishaalikud = "a, e, i, o, u"
    kaashaalikud = "b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, x, z, w, y"
    taishaalikute_arv = book.count(taishaalikud)
    konsonantide_arv = book.count(kaashaalikud)
    if taishaalikute_arv == konsonantide_arv:
        return True
    elif taishaalikute_arv - konsonantide_arv == 1:
        return True
    elif konsonantide_arv - taishaalikute_arv == 1:
        return True
    return False
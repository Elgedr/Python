"""Book_sortation."""


def add_book_to_category(book: str, category: str, categorised_books: dict) -> dict:
    """1 funktsioon."""
    categorised_books = {"spell books": [],
                         "history books": [],
                         "relics books": [],
                         "potion books": [],
                         "other books": []}
    for book in categorised_books:
        if category in categorised_books:
            categorised_books[category].append(book)
        elif category not in categorised_books:
            categorised_books[category].append(book)
    return categorised_books
    # if is_spell_book(book) is True:
    #     categorised_books["spell book"].append(book)
    # elif is_history_book(book) is True:
    #     categorised_books["history books"].append(book)
    # elif is_relics_book(book) is True:
    #     categorised_books["relics books"].append(book)
    # elif is_potion_book(book) is True:
    #     categorised_books["potion books"].append(book)
    # else:
    #     categorised_books["other books"].append(book)
    # return categorised_books


def booksortation(books: list) -> dict:
    """Peamine funktsioon."""
    add_book_to_category(books)

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


if __name__ == '__main__':
    # All True.
    print(is_spell_book('*kana*'))
    print(is_history_book('This Is A History Book'))
    print(is_relics_book('ThE StAfF'))
    print(is_potion_book('The Banana Juice'))
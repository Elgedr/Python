"""Book_sortation."""


def booksortation(books: list) -> dict:
    """Peamine funktsioon."""
    new_sorted = {}
    for i in range(len(books)):
        if is_spell_book(books[i]) is True:
            new_sorted = add_book_to_category(books[i], "spell book", new_sorted)
        elif is_history_book(books[i]) is True:
            new_sorted = add_book_to_category(books[i], "history book", new_sorted)
        elif is_relics_book(books[i]) is True:
            new_sorted = add_book_to_category(books[i], "relics book", new_sorted)
        elif is_potion_book(books[i]) is True:
            new_sorted = add_book_to_category(books[i], "potion book", new_sorted)
    else:
        new_sorted = add_book_to_category(books[i], "other", new_sorted)

    for i in new_sorted:
        new_sorted[i].sort()
    return new_sorted


def add_book_to_category(book: str, category: str, categorised_books: dict) -> dict:
    """1 funktsioon."""
    if category in categorised_books:
        categorised_books[category].append(book)
        return categorised_books
    else:
        categorised_books[category] = []
        categorised_books[category].append(book)
        return categorised_books


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

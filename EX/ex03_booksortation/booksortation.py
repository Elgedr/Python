"""Book_sortation."""


def booksortation(books: list) -> dict:
    """Peamine funktsioon."""
    new_sorted = {}
    for i in range(len(books)):
        if is_spell_book(books[i]) is True:
            new_sorted = add_book_to_category(books[i], "spell books", new_sorted)
        elif is_history_book(books[i]) is True:
            new_sorted = add_book_to_category(books[i], "history books", new_sorted)
        elif is_relics_book(books[i]) is True:
            new_sorted = add_book_to_category(books[i], "relics books", new_sorted)
        elif is_potion_book(books[i]) is True:
            new_sorted = add_book_to_category(books[i], "potion books", new_sorted)
        else:
            new_sorted = add_book_to_category(books[i], "other books", new_sorted)

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
    if len(book) >= 2 and book.startswith("*") and book.endswith("*"):
        return True
    return False


def is_history_book(book: str) -> bool:
    """3 funktsioon."""
    world = book.split()
    for i in world:
        if i[0].islower():
            return False
        if i[0].isupper():
            pass
    return True


def is_relics_book(book: str) -> bool:
    """4 funktsioon."""
    for i in range(1, len(book)):
        if book[i].isupper() and book[i - 1].isupper():
            return False
        elif book[i].islower() and book[i - 1].islower():
            return False
        elif book[i].islower() and book[i - 1] == " " and book[i - 2].isupper():
            return False
        elif book[i].isupper() and book[i - 1] == " " and book[i - 2].islower():
            return False
    return True


def is_potion_book(book: str) -> bool:
    """5 funktsioon."""
    taishaalikud = "aeiou"
    kaashaalikud = "bcdfghjklmnpqrstvxzwy"
    taishaalikute_arv = 0
    konsonantide_arv = 0
    small = book.lower()
    for letter in small:
        if letter in taishaalikud:
            taishaalikute_arv = taishaalikute_arv + 1
        elif letter in kaashaalikud:
            konsonantide_arv = konsonantide_arv + 1
    if taishaalikute_arv == konsonantide_arv:
        return True
    elif taishaalikute_arv - konsonantide_arv == 1:
        return True
    elif konsonantide_arv - taishaalikute_arv == 1:
        return True
    return False


if __name__ == '__main__':
    print(booksortation(["*kana*", 'This Is A History Book', 'ThE StAfF']))

"""Messenger."""


class User:
    """User class."""

    def __init__(self, name):
        """User constructor."""
        self.name = name  # kasutaja nimi


class Chat:
    """Chat class."""

    def __init__(self, name, users):
        """Chat constructor."""
        self.name = name  # vestluse nimi
        self.users = users  # nimekiri kasutajatest, kes vestluses on - koosneb User objektidest
        self.messages = []  # nimekiri sõnumitest, mis vestlusesse kirjutatud on - koosneb Message objektidest


class Message:
    """Message class."""

    def __init__(self, user, content):
        """Message constructor."""
        self.user = user  # sõnumi autor
        self.content = content  # sõnumi sisu
        self.reactions = 0  # sõnumi reaktsioonide kogus


def write_message(userrrr: User, chat: Chat, content: str) -> None:
    """Write a message to given chat."""
    if userrrr in chat.users:
        new_message = Message(userrrr, content)
        chat.messages.append(new_message)


def delete_message(chattt: Chat, messageee: Message) -> None:
    """Delete message from chat."""
    if messageee in chattt.messages:
        chattt.messages.remove(messageee)


def get_messages_by_user(userrr: User, chattt: Chat) -> list:
    """Get messages by user in chat."""
    messages = []
    for messag in chattt.messages:
        if userrr.name in messag.user.name:
            messages.append(messag)
    return messages


def react_to_last_message(chattt: Chat) -> None:
    """Add reaction to last message in chat."""
    if len(chattt.messages) > 0:
        chattt.messages[-1].reactions = chattt.messages[-1].reactions + 1


def find_most_reacted_message(chat: Chat) -> Message:
    """Find the most reacted message in chat."""
    count = 0
    res = Message
    for mes in chat.messages:
        if mes.reactions >= count:
            count = mes.reactions
            res = mes
    return res


def count_reactions_in_chat(chattt: Chat) -> int:
    """Count all reactions in chat."""
    res = []
    for mes in chattt.messages:
        res.append(mes.reactions)
    result = sum(res)
    return result


def count_reactions_by_chat(chats: list) -> dict:
    """Count reactions in every chat."""
    res = {}
    for chat in chats:
        res[chat.name] = count_reactions_in_chat(chat)
    return res


if __name__ == '__main__':
    user1 = User("Alma")
    user2 = User("Ago")
    chat = Chat("Python 2020", [user1, user2])

    write_message(user1, chat, "Parim kohvipiim")
    write_message(user2, chat, "Eestimaa farmidest")
    write_message(user2, chat, "Piim")
    write_message(user1, chat, "Farmi")
    for message in chat.messages:
        print(f"{message.user.name}: {message.content}")
        # Alma: Parim kohvipiim
        # Ago: Eestimaa farmidest
        # Ago: Piim
        # Alma: Farmi

    to_be_deleted = get_messages_by_user(user2, chat)
    for message in to_be_deleted:
        delete_message(chat, message)
    for message in chat.messages:
        print(f"{message.user.name}: {message.content}")
        # Alma: Parim kohvipiim
        # Alma: Farmi

    react_to_last_message(chat)
    print(chat.messages[0].reactions)  # 0
    print(chat.messages[-1].reactions)  # 1

    most_reacted = find_most_reacted_message(chat)
    print(f"{most_reacted.content}: {most_reacted.reactions}")  # Farmi: 1

    print(count_reactions_in_chat(chat))  # 1
    print(count_reactions_by_chat([chat]))  # {"Python 2020": 1}

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


def find_most_reacted_message(chattt: Chat) -> Message:
    """Find the most reacted message in chat."""
    mes = {}
    for mess in chattt.messages:
        mes[mess] = mess.reactions
    res = max(mes.items(), key=lambda x: x[1])[0]
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
        res[chat] = count_reactions_in_chat(chat)
    return res

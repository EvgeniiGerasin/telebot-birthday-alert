from dataclasses import dataclass

@dataclass
class TextMessage:

    HELP = (
        '\n'
        '/help - помощь\n'
        '/all - ДР за год\n'
        '/month - ДР в текущем месяце\n'
    )
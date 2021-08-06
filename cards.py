"""Module cards"""


from termcolor import cprint
from colorama import init
from re import split
init()
card_ranks = [str(x) for x in ['Ace', *range(2, 11), 'Jack', 'Queen', 'King']]
format_cards = True
card_symbols = {'♠': 'Spades', '♥': 'Hearts', '♦': 'Diamonds', '♣': 'Clubs'}
space = lambda a: a * ' '


def suit(symbol: str) -> list:
    """adds styling to all elements in the list

    """
    new_suit = []
    for x in card_ranks:
        string = f'{x}{space(6-len(x))}{symbol}'
        new_suit.append(string)
    return new_suit


cards = suit('♠') + suit('♥') + suit('♦') + suit('♣')


def cardify(card: str):
    """Formats an element as a playing card

    """
    global card_symbols
    global format_cards
    print()
    if format_cards:
        color = 'red' if '♥' in card or '♦' in card else 'grey'
        reverse = split(' +', card)
        cprint(card, color, 'on_white')
        cprint(space(7), color, 'on_white')
        cprint(f'{space(3)}{reverse[1]}{space(3)}', color, 'on_white')
        cprint(space(7), color, 'on_white')
        cprint(f'{reverse[1]}{space(6-len(reverse[0]))}{reverse[0]}', color, 'on_white')
    else:
        simple = split(' +', card)
        print(f'{simple[0]} of {card_symbols[simple[1]]}')
    print()
"""Module dice"""


from secrets import randbelow
from colorama import init
from termcolor import cprint
from time import sleep
from tqdm import tqdm
from prettytable import PrettyTable

init()
dice_name = ''
preperation_round = PrettyTable(['Preperation Round'])
preperation_round.add_rows([
    [
        'In the preparation round, you will determine how much each player will get.'
    ],
    [
        'You must enter a valid integer or else you will be given the default value.'
    ],
])
default_values = PrettyTable(['Player', 'Default value'])
default_values.add_rows([[dice_name, '$1000'], ['CPU', '$1250']])
main_round = PrettyTable(['Main Round'])
main_round.add_rows([
    [
        'Now that you have completed the preparation round, we can get into the main game.'
    ],
    [
        'At the beginning of each round, you will have a bet. The CPU will match your bet.'
    ],
    [
        'If your bet is higher than the CPU\'s funds, the CPU will bet all its remaining funds.'
    ],
    ['If you wish to bet all of your funds, input "all".'],
    ['If you wish to quit, input "quit".'],
    ['Both you and the CPU will roll two dice.'],
    ['Your score is equivalent to the sum of the dice.'],
    ['Whoever achieves the highest score will take the entire pot.'],
    ['If there is a tie, the pot will be split equally.'],
])


def roll(entity: str) -> int:
    """Rolls two dice, returning the sum of the rolls

    """
    one = 1 + randbelow(6)
    two = 1 + randbelow(6)
    for i in tqdm(range(2), desc=f'{entity} Rolling', ascii=False, ncols=100):
        sleep(0.5)
    print(f'''Dice 1: {one}
Dice 2: {two}''')
    return (one + two)


def prep_dice(sum: int, player='') -> int:
    print(f'How much money would you like {player} to start with?')
    try:
        player_sum = int(input('$'))
    except:
        return sum
    return sum if player_sum < 1 else player_sum


def main_game(player: str, player_sum: int, bot_sum: int) -> list:
    turns = 0
    balance = PrettyTable(['Player', 'Balance'])
    while player_sum > 0 and bot_sum > 0:
        balance.add_rows([[player, f'${player_sum}'], ['CPU', f'${bot_sum}']])
        print(balance)
        balance.clear_rows()
        bet = input(f'{player}\'s bet: $').lower().strip()
        if bet == 'all': bet = player_sum
        elif bet == 'quit': break
        try:
            if not player_sum >= (bet := int(bet)) > 0: raise Exception
        except:
            cprint('Enter a valid bet', 'red')
            continue
        player_sum -= bet
        if bot_sum < bet: pot, bot_sum = bot_sum + bet, 0
        else: pot, bot_sum = bet * 2, bot_sum - bet
        print(f'Pot is ${pot:,}')
        input('Press enter to roll')
        player_score = roll('You are')
        sleep(1)
        bot_score = roll('CPU is')
        if player_score > bot_score: player_sum += pot
        elif player_score < bot_score: bot_sum += pot
        else:
            pot //= 2
            bot_sum += pot
            player_sum += pot
            pot = 0
        turns += 1

    return [bot_sum, player_sum, turns]


def recap(info_list: list):
    bot_sum, player_sum, turns = info_list
    if bot_sum == 0:
        print(f'''You won in {turns} turns.
Your remaining balance was ${player_sum:,}.''')
    elif player_sum == 0:
        print(f'''The CPU won in {turns} turns
The CPU\'s remaining balance was ${bot_sum:,}.''')

'''Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which '''

import random
random.seed()

bank_account = 1000000
bet_amount = 0
bet_color = None
bet_number = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


def take_bet():
    global bank_account
    color_bet = 0
    number_bet = 0
    color = input("Insert bet color (red / black / none): ")
    if color == "red" or color == "black":
        color_bet = input("Insert bet value on color: ")
        if color_bet.isdigit():
            pass
        else:
            color_bet = 0
    else:
        color = "none"
    number = input("Insert bet number (1-37/ none): ")
    if number.isdigit():
        if int(number) >= 1 and int(number) <= 37:
            number_bet = input("Insert bet value on number: ")
            if number_bet.isdigit():
                pass
            else:
                number_bet = 0
        else:
            number = "none"
    else:
        number = "none"
    bets = [color, color_bet, number, number_bet]
    if (int(color_bet) + int(number_bet)) <= bank_account:
        return(bets)
    else:
        print("Not enough money. Bet:", int(color_bet) + int(number_bet))
        print("Account:", bank_account)
        return("none")


def roll_ball():
    rand_number = random.randint(1, 38)
    if rand_number in red:
        print("The outcome was", rand_number, "and it is in the color red")
    elif rand_number in black:
        print("The outcome was", rand_number, "and it is in the color black")
    else:
        print("The outcome was", rand_number, "and it is in the color green")
    return rand_number


def check_results(rand_number, bet_number, bet_color):
    if rand_number == bet_number:
        if bet_color == "red":
            if rand_number in red:
                return 4
            else:
                return 3
        elif bet_color == "black":
            if rand_number in black:
                return 4
            else:
                return 3
    elif bet_color == "red":
        if rand_number in red:
            return 2
    elif bet_color == "black":
        if rand_number in black:
            return 2
    return 1


def payout(game_outcome, small_bet, big_bet):
    global bank_account
    if game_outcome == 4:
        won_amount = int(small_bet) + int(big_bet) * 35
    elif game_outcome == 3:
        won_amount = - int(small_bet) + int(big_bet) * 35
    elif game_outcome == 2:
        won_amount = int(small_bet) - int(big_bet)
    else:
        won_amount = - int(small_bet) - int(big_bet)
    bank_account += won_amount
    return(won_amount)


def restart():
    restart = input("Play again? (y/n):")
    if restart == "y":
        play_game()
    else:
        return


def play_game():
    global bank_account
    bets = take_bet()

    if bets != "none":
        rand_number = roll_ball()
        game_outcome = check_results(rand_number, bets[2], bets[0])
        account_change = payout(game_outcome, bets[1], bets[3])
        print("Your bank statement:", bank_account, "(", account_change, ")")

    restart()
    return


if __name__ == '__main__':
    play_game()

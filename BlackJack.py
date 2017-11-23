# A blackjack program, Player versus dealer.
# only setup for 2 players as traditionally
# blackjack is between player and dealer.

import random
# hands as global variables since they need
# to be stored reliably and addressed by multiple
# functions
playerHand = []
dealerHand = []


def main():
    print('\tWelcome to the table.\nYour hand will '
          'be displayed for you in an abbreviated '
          'form as you play,\nSuits are  '
          'represented as such: (C)lubs, '
          '(S)pades (H)earts, (D)iamonds\n'
          'Try to get as close as you can to 21 '
          'without going over.\n')
    # calls to draw 2 cards for each player
    i = 0
    while i < 2:
        player()
        dealer()
        i += 1
    while True:
        print(str(playerHand) + '\nTotal: ' +
              str(points(playerHand)))
        choice = str(input('Hit or stay?\n'))
        if choice.lower()[0] == 'h':
            player()
            dealer()
        elif choice.lower() == 's':
            print(str(playerHand) + '\n' +
                  str(points(playerHand)) +
                  ' points in total.')
            winner()
        else:
            print(str(playerHand) + '\n' +
                  str(points(playerHand)) +
                  ' points in total.')
            winner()
    winner()


def getSuite():
    val = random.randint(1, 4)

    if val == 1:
        word = 'Clubs'
    elif val == 2:
        word = 'Spades'
    elif val == 3:
        word = 'Hearts'
    else:
        word = 'Diamonds'
    return word


def getCard():
    val = random.randint(0, 12)
    words = ['Ace', '2', '3', '4', '5',
             '6', '7', '8', '9',
             '10', 'Jack', 'Queen', 'King']
    return words[val]


def points(hand):
    total = 0
    aces = False
    for card in hand:
        # first 5 cases deal with
        # invalid int literals
        if card[0] == 'A':
            # special handling as aces are
            # soft 11's
            total += 11
            aces = True

        elif card[0] == '1':
            # only place a 1 appears is as
            # first character of '10'
            total += 10
        elif card[0] == 'J':
            total += 10
        elif card[0] == 'Q':
            total += 10
        elif card[0] == 'K':
            total += 10
        # anything 2-10 can become an int
        elif 2 <= int(card[0]) <= 10:
            total += int(card[0])
        if total > 21 and aces == True:
            total -= 10
    return total


def dealer():
    number = getCard()
    suite = getSuite()
    total = points(dealerHand)
    if total <= 16:
        print('Dealer draws a card.')
        if number == '10':
            dealerHand.append('10' + suite[0])
        else:
            dealerHand.append(number[0] +
                              suite[0])
    else:
        print('Dealer holds.')


def player():
    number = getCard()
    suite = getSuite()
    print('You drew the ' + str(number) +
          ' of ' + suite + '.')
    if number == '10':
        playerHand.append('10' + suite[0])
    else:
        playerHand.append(number[0] +
                          suite[0])
    if points(playerHand) >= 21:
        # 21 is an automatic endgame
        # anything higher is an automatic loss
        winner()


def winner():
    playPts = points(playerHand)
    if playPts <= 21:
        while points(dealerHand) <= 16:
            dealer()
    housePts = points(dealerHand)
    verdict = ('You have ' + str(playPts) +
               ' points, The House has ' +
               str(housePts) + ', ')
    if 21 >= playPts > housePts:
        verdict += 'you win!'
    elif housePts > 21 >= playPts:
        verdict += 'you win!'
    elif playPts > 21:
        verdict += 'you lose.'
    elif housePts >= playPts:
        verdict += 'you lose.'
    else:
        verdict += 'you lose.'
    print(verdict)
    print('Dealer reveals:\n' + str(dealerHand))
    # pause for response if run from outside
    # compiler.
    str(input('Any key to exit\n'))
    exit()
main()

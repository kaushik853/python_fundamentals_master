'''
Code a game of rock paper scissors.

'''

import random
# function to get hand based on number
# the function should take in a number and return the string representation of the hand
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    if hand == 0:
        return 'scissor'
    elif hand == 1:
        return 'rock'
    else:
        return 'paper'

    # for example if the variable hand is 0, it should return the string "scissor"

# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, player):
    if (computer == 'rock' and player == 'paper') or (computer == 'scissor' and player == 'rock') or (computer == 'paper' and player == 'scissor'):
        return 'You Won!'
    # if (player == 'rock' and computer == 'paper') or (player == 'scissor' and computer == 'rock') or (player == 'paper' and computer == 'scissor'):
    #     print('You lost :(')
    else:
        return 'You lost!'




'''
Start here
'''
user_input = int(input("please enter a number between 0 and 2: "))
comp_input = random.randint(0, 2)
while user_input == comp_input:
    comp_input = random.randint(0, 2)
user_hand = get_hand(user_input)
comp_hand = get_hand(comp_input)
print(user_hand)
print(comp_hand)
winner = determine_winner(comp_hand, user_hand)
print(winner)
#print('thankx for playing')

# take in a number 0-2 from the user that represents their hand

# generate a random number 0-2 to use for the computer's hand

# call the function get_hand to get the string representation of the user's hand

# call the function get_hand to get the string representation of the computer's hand

# call the function determine_winner to figure out the winner

# print out the player hand and computer hand

# print out the winner

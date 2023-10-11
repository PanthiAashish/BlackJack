# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
user_hand = draw_starting_hand("YOUR")

var_to_replace_break = True
while user_hand < 21 and var_to_replace_break:
  user_input = input('You have ' + str(user_hand) + ". Hit (y/n)? ")
  if user_input == 'y':
    user_hand = user_hand + draw_card()
  elif user_input == 'n':
    var_to_replace_break = False
  else:
    print("Sorry I didn't get that.")
print_end_turn_status(user_hand)

dealer_hand = draw_starting_hand("DEALER")

while dealer_hand < 17:
  dealer_hand = dealer_hand + draw_card()
print_end_turn_status(dealer_hand)

print_end_game_status(user_hand, dealer_hand)
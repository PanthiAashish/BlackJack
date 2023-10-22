
from blackjack_helper import *
from unit_test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):


  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
    self.assertEqual(get_print(print_card_name, 3), "Drew a 3\n")
    self.assertEqual(get_print(print_card_name, 4), "Drew a 4\n")
    self.assertEqual(get_print(print_card_name, 5), "Drew a 5\n")
    self.assertEqual(get_print(print_card_name, 6), "Drew a 6\n")
    self.assertEqual(get_print(print_card_name, 7), "Drew a 7\n")
    self.assertEqual(get_print(print_card_name, 9), "Drew a 9\n")
    self.assertEqual(get_print(print_card_name, 10), "Drew a 10\n")
    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 12), "Drew a Queen\n")
    self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")
    self.assertEqual(get_print(print_card_name, 0), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, 14), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, -1), "BAD CARD\n")
    
  def test_draw_card(self):
    self.assertEqual(mock_random([1], draw_card) ,11)
      # self.assertEqual(get_print(draw_card, mock_random[1]), "Drew an Ace\n")
    self.assertEqual(mock_random([2], draw_card) ,2)
    self.assertEqual(mock_random([3], draw_card) ,3)
    self.assertEqual(mock_random([4], draw_card) ,4)
    self.assertEqual(mock_random([5], draw_card) ,5)
    self.assertEqual(mock_random([6], draw_card) ,6)
    self.assertEqual(mock_random([7], draw_card) ,7)
    self.assertEqual(mock_random([8], draw_card) ,8)
    self.assertEqual(mock_random([9], draw_card) ,9)
    self.assertEqual(mock_random([10], draw_card) ,10)
    self.assertEqual(mock_random([11], draw_card) ,10)
    self.assertEqual(mock_random([12], draw_card) ,10)
    self.assertEqual(mock_random([13], draw_card) ,10)
    
  def test_print_header(self):
    self.assertEqual(get_print(print_header, 'HELLO WORLD') ,'-----------\nHELLO WORLD\n-----------')
    self.assertEqual(get_print(print_header, 'YOUR TURN') , '-----------\nYOUR TURN\n-----------')
    self.assertEqual(get_print(print_header, 'DEALER TURN') , '-----------\nDEALER TURN\n-----------')
    self.assertEqual(get_print(print_header, '') , '-----------\n\n-----------')

  def test_draw_starting_hand(self):
    self.assertEqual(mock_random([3, 5], draw_starting_hand, 'DEALER'), 8)
    self.assertEqual(mock_random([1, 1], draw_starting_hand, ''), 22)
    self.assertEqual(mock_random([13, 13], draw_starting_hand, 'YOUR'), 20)
    self.assertEqual(mock_random([11, 10], draw_starting_hand, 'DEALER'), 20)
    self.assertEqual(mock_random([12, 12], draw_starting_hand, 'DEALER'), 20)
    self.assertEqual(mock_random([13, 1], draw_starting_hand, 'DEALER'), 21)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, 'DEALER'), 8)
    self.assertEqual(mock_random([2, 3], draw_starting_hand, 'DEALER'), 5)
    self.assertEqual(mock_random([3, 4], draw_starting_hand, 'DEALER'), 7)
    self.assertEqual(mock_random([4, 5], draw_starting_hand, 'DEALER'), 9)
    self.assertEqual(mock_random([5, 6], draw_starting_hand, 'DEALER'), 11)
    self.assertEqual(mock_random([6, 7], draw_starting_hand, 'DEALER'), 13)
    self.assertEqual(mock_random([8, 9], draw_starting_hand, 'DEALER'), 17)
    self.assertEqual(mock_random([9, 10], draw_starting_hand, 'DEALER'), 19)


  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status, 17) ,'Final hand: 17.')
    self.assertEqual(get_print(print_end_turn_status, 21) ,'Final hand: 21.\nBLACKJACK!')
    self.assertEqual(get_print(print_end_turn_status, 22) ,'Final hand: 22.\nBUST.')
    self.assertEqual(get_print(print_end_turn_status, 4) ,'Final hand: 4.')
    self.assertEqual(get_print(print_end_turn_status, 5) ,'Final hand: 5.')
    self.assertEqual(get_print(print_end_turn_status, 6) ,'Final hand: 6.')
    self.assertEqual(get_print(print_end_turn_status, 7) ,'Final hand: 7.')
    self.assertEqual(get_print(print_end_turn_status, 10) ,'Final hand: 10.')
    self.assertEqual(get_print(print_end_turn_status, 11) ,'Final hand: 11.')
    self.assertEqual(get_print(print_end_turn_status, 12) ,'Final hand: 12.')
    self.assertEqual(get_print(print_end_turn_status, 13) ,'Final hand: 13.')
    self.assertEqual(get_print(print_end_turn_status, 15) ,'Final hand: 15.')
    self.assertEqual(get_print(print_end_turn_status, 16) ,'Final hand: 16.')
    self.assertEqual(get_print(print_end_turn_status, 18) ,'Final hand: 18.')
    self.assertEqual(get_print(print_end_turn_status, 19) ,'Final hand: 19.')
    self.assertEqual(get_print(print_end_turn_status, 20) ,'Final hand: 20.')
    self.assertEqual(get_print(print_end_turn_status, 8) ,'Final hand: 8.')
    self.assertEqual(get_print(print_end_turn_status, 9) ,'Final hand: 9.')
    self.assertEqual(get_print(print_end_turn_status, 14) ,'Final hand: 14.')


  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_game_status, 17,18) ,'-----------\nGAME RESULT\n-----------\nDealer wins!')
    self.assertEqual(get_print(print_end_game_status, 20,21) ,'-----------\nGAME RESULT\n-----------\nDealer wins!')
    self.assertEqual(get_print(print_end_game_status, 22,22) ,'-----------\nGAME RESULT\n-----------\nDealer wins!')
    self.assertEqual(get_print(print_end_game_status, 22,17) ,'-----------\nGAME RESULT\n-----------\nDealer wins!')
    self.assertEqual(get_print(print_end_game_status, 23,27) ,'-----------\nGAME RESULT\n-----------\nDealer wins!')
    self.assertEqual(get_print(print_end_game_status, 18,17) ,'-----------\nGAME RESULT\n-----------\nYou win!!')
    self.assertEqual(get_print(print_end_game_status, 19,18) ,'-----------\nGAME RESULT\n-----------\nYou win!!')
    self.assertEqual(get_print(print_end_game_status, 21,18) ,'-----------\nGAME RESULT\n-----------\nYou win!!')
    self.assertEqual(get_print(print_end_game_status, 10,22) ,'-----------\nGAME RESULT\n-----------\nYou win!!')
    self.assertEqual(get_print(print_end_game_status, 17,17) ,'-----------\nGAME RESULT\n-----------\nPush.')
    self.assertEqual(get_print(print_end_game_status, 19,19) ,'-----------\nGAME RESULT\n-----------\nPush.')
    self.assertEqual(get_print(print_end_game_status, 2,21) ,'-----------\nGAME RESULT\n-----------\nPush.')



if __name__ == '__main__':
    unittest.main()
from unittest import TestCase, main
from unittest.mock import patch
from integration_test_helper import run_test

class TestBlackjack(TestCase):

    # @patch('blackjack_helper.randint')
    # @patch('builtins.input')

#     # Make sure all your test functions start with test_ 
#     # Follow indentation of test_example
#     # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_higher(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.
        '''
        output = run_test([4, 5, 7], ['y', 'n'], [4, 5, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 5\n" \
                   "You have 9. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 5\n" \
                   "Dealer has 9.\n" \
                   "Drew a 9\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_bust(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand more than 21.
        The dealer wins as both user and dealer are bust.
        '''
        output = run_test([10, 7, 8], ['y'], [10, 6, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 6\n" \
                   "Dealer has 16.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 27.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_lower(self, input_mock, randint_mock):
        '''
        Dealer has hand smaller than 21 and user busts.
        The dealer wins as user is bust.
        '''
        output = run_test([10, 7, 8], ['y'], [10, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 7\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_blackjack_user_no_bust(self, input_mock, randint_mock):
        '''
        Dealer has Blackjack and user is not bust(user inputs 'n' when prompted)
        Dealer wins by having blackjack
        '''
        output = run_test([10, 7], ['n'], [10, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_blackjack_user_bust(self, input_mock, randint_mock):
        '''
        Dealer has Blackjack and user is bust(user inputs 'y' when prompted)
        Dealer wins by having blackjack and user being bust
        '''
        output = run_test([10, 7,11], ['y'], [10, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 7\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a Jack\n" \
                   "Final hand: 27.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew an Ace\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_higher(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
        '''
        output = run_test([11, 12], ['n'], [1,7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a Queen\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 7\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_dealer_bust(self, input_mock, randint_mock):
        '''
        Dealer receive hand with value more than 21 and user has value less than 21
        User wins as the dealer is bust
        Also checked what happens when user replies with other character apart from y and n.
        '''
        output = run_test([11, 12],['a','n'],[1,1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a Queen\n" \
                   "You have 20. Hit (y/n)? a\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
   
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_blackjack_dealer_bust(self, input_mock, randint_mock):
        '''
        Dealer receive hand with value more than 21 and user has hand value 21
        User wins with Blackjack as the dealer is bust
        '''
        output = run_test([7, 7, 7],['y'],[1,1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 7\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_blackjack_dealer_no_bust(self, input_mock, randint_mock):
        '''
        Dealer receive hand with value less than 21 and user has hand value 21
        User wins with Blackjack as the dealer's hand is lower than 21
        '''
        output = run_test([7, 7, 7],['y'],[10,8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 7\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew an 8\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_user_equal(self, input_mock, randint_mock):
        '''
        Dealer and user both have equal hand but it is less than 21
        IT gets tie and 'Push' is printed
        '''
        output = run_test([6, 6, 6],['y','n'],[6,6,6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 6\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 6\n" \
                   "Dealer has 12.\n" \
                   "Drew a 6\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_user_blackjack(self, input_mock, randint_mock):
        '''
        Both user and dealer has same hand value of 21(both get Blackjack)
        Games gets tied and Push is printed
        '''
        output = run_test([7, 7, 7],['y'],[10,6,5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 7\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 6\n" \
                   "Dealer has 16.\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)


#     # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
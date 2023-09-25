class Table(object):

    def __init__(self, player, funds=100):

        self.dealer = dealer()
        self.player = player(player, funds)
        self.deck = deck

        self.table_setup()

    def table_setup(self):

        self.deck.shuffle()

        self.player.place_bet()

        self.deal_card(self.player)
        self.deal_card(self.dealer)
        self.deal_card(self.player)
        
        self.calculate_score(self.player)
        self.calculate_score(self.dealer)

    def main(self):

        while True:
            print()
            print(self)
            player_move = self.player.hit_or_miss()
            if player_move is True:
                self.deal_card(self.player)
                self.calculate_score(self.player)
            elif player_move is False:
                self.dealer_hit()

    def dealer_hit(self):

        score = self.dealer.score
        while True:
            if score < 17:
                self.deal_card(self.dealer)
                self.calculate_score(self.dealer)
                print(self)
            elif score >= 17:
                self.check_final_score()

    def __str__(self): 

        dealer_hand = [card for card, value in self.dealer.hand]
        player_hand = [card for card, value in self.player.hand]

        print("Dealer hand : {}".format(dealer_hand))
        print("Dealer score : {}".format(self.dealer.score))
        print()
        print("{}'s hand : {}".format(self.player.name, player_hand))
        print("{}'s score : {}".format(self.player.name, self.player.score))
        print()

    def deal_card(self, player):

        card = self.deck.stack.pop()
        player.hand.append(card)

    def calculate_score(self, player):

        ace = False
        score = 0
        for card in player.hand:
            if card[1] == 1 and not ace:
                ace = True
                card = ('A', 11)
            score += card[1]
        player.score = score
        if player.score > 21 and ace:
            player.score -= 10 
            score = player.score
        self.check_win(score, player)
        return
    
    def check_win(self, score, player):
        if score > 21:
            print()
            print(self)
            print("{} busts".format(player.name))
            print()
            self.end_game()
        elif score == 21:
            print(self)
            print("{} blackjack achieved!".format(player.name))
        else:
            return
    
    def check_final_score(self):

        dealer_score = self.dealer.score
        player_score = self.player.score

        if dealer_score > player_score:
            print("Dealer has won!")
            self.end_game
        else:
            print("{} is the winner!".format(self.player.name))
            self.end_game
        
       

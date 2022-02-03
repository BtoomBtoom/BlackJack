from library import *



#money_bet
money_bet = 0

#play_on = true
play_again = True

# set up
new_deck = Deck()
new_deck.suffle()
bank_roll = Bank(int(input("How much do you want to play?: ")))

def hit_card_player():
    global new_deck
    global player_cards
    global player_sum
    new_card = new_deck.hit()
    player_cards.append(new_card)
    player_sum += values[new_card.rank]
    print(f"You hit a ", end="")
    print(new_card,end="")
    print(f", sum now is {player_sum}")
    print("\n"*2)

def hit_card_dealer():
    global new_deck
    global dealer_cards
    global dealer_sum
    new_card = new_deck.hit()
    dealer_cards.append(new_card)
    dealer_sum += values[new_card.rank]
    print(f"Dealer hit a ", end="")
    print(new_card,end="")
    print(f", sum now is {dealer_sum}")
    print("\n" * 2)

while play_again:
    # dealer_cards
    dealer_cards = []
    dealer_sum = 0

    # player_cards
    player_cards = []
    player_sum = 0
    play_on = True


    # bet_money
    while True:
        money_bet = int(input("How much do you want to bet?: "))
        #check ip money bet > money in the bank
        if money_bet > bank_roll.amount:
            print("can not bet amount exceeding your bank_roll")
        else:
            break

    # player hit 2 and show 2


    # new_card = new_deck.hit()
    # player_cards.append(new_card)
    # player_sum+=values[new_card.rank]
    # print(f"You hit a ",end="")
    # print(new_card+f", sum now is {player_sum}")
    hit_card_player()
    # new_card = new_deck.hit()
    # player_cards.append(new_card)
    # player_sum += values[new_card.rank]
    # print(f"You hit a ",end="")
    # print(new_card+f", sum now is {player_sum}")
    hit_card_player()


    # dealer hit 2 and show 1
    new_card = new_deck.hit()
    dealer_cards.append(new_card)
    dealer_sum +=values[new_card.rank]
    new_card = new_deck.hit()
    dealer_cards.append(new_card)
    dealer_sum += values[new_card.rank]
    print(f"Dealer hit 1 hidden card, and a ",end="")
    print(new_card)


    # check if player win by having sum of 21 because the first two times hits's biggest number is 21

    if(player_sum==21):
            bank_roll.win(money_bet)
            print(f"Player win, you have {bank_roll.amount} in bank")
            if (input("Do you want to bet again?yes/no: ")).lower()=="yes":
                play_on = False
            elif (input("Do you want to bet again?yes/no: ")).lower()=="no":
                break


    #hit or stay turn
    while play_on:
        #player_turn

        # hit or stay turn for player
        while True:
            #player hit
            enter = input("Do you want to hit?: ").lower()


            if(enter=="yes"):
                #hit a card
                hit_card_player()
                print(f"\n{new_deck.number()} cards left in the deck")



                #if player already win by having sum of 21
                if (player_sum == 21):
                    #add winning money to bank
                    bank_roll.win(money_bet)
                    print(f"Player win, you have {bank_roll.amount} in bank")
                    #bet gain ??
                    enter_1 = input("Do you want to bet again?: ").lower()
                    if enter_1 == "yes":
                        #if want to bet again, play_again = true for bet again, break the  "hit or stay turn for player"
                        play_gain = True
                        break
                    elif enter_1 == "no":
                        #if dont want to bet again
                        play_again = False
                        break


                #if already lose by having sum > 21
                if player_sum > 21:
                    #player lose his money_bet
                    bank_roll.lose(money_bet)

                    #if player lose money_bet and bank is empty, player lose, the game is over
                    if bank_roll.amount == 0:
                        #player lose, break the  "hit or stay turn for player", break the play_again loop too for end game
                        #play_again = False #break the play_again loop
                        print("Your bank is 0, you lose, game over!!!!!")
                        break               #break the the hit or stay turn for player

                    #if player lose bet money but still have money in bank
                    print(f"Player lose, you have {bank_roll.amount} in bank")

                    #want to bet again?
                    enter_2 = input("Do you want to bet again?: ").lower()
                    #if want to bet again
                    if enter_2 == "yes":
                        #keep the play_again loop continue, break the  "hit or stay turn for player"
                        play_again = True
                        break
                    #if dont want to bet again
                    elif enter_2 == "no":
                        #stop the play_again loop, break the  "hit or stay turn for player"
                        play_again = False
                        break

            #if dont want to hit another card
            elif enter=="no":
                break

        #player already win by having sum of 21,bypass the dealer_turn and
        #they already decide to or not to bet again up there by assign true false to "play_again"
        if  player_sum == 21:
            #break the hit or stay turn(play_on), come back top to play_again?
            break


        #player already lose by having sum > 21 and still have money in bank ,bypass the dealer turn and
        #they already decide to or not to bet again up there by assign true false to "play_again"
        if player_sum > 21:
            # break the hit or stay turn(play_on), come back top to play_again?
            break



        #if player already both lose by having sum > 21 and have 0 money in bank
        #break the hit or stay turn for player and also break the play_again loop, end game
        if bank_roll.amount == 0:
            break   #break the hit or stay turn(play_on)



        #if player_sum<21, it's the dealer's turn

        #dealer_turn
        print("Dealer has ", end="")
        print(dealer_cards[0], end =" and ")
        print(dealer_cards[1])
        print("Dealer starts: \n\n\n")

        #loop for dealer_turn, keep hit card until dealer win by having sum>player and <=21
        # or until the dealer lose by having sum >21
        while True:
            #pick card
            hit_card_dealer()
            print(f"\n{new_deck.number()} cards left in the deck")

            #if dealer still has sum < player_sum
            if(dealer_sum<player_sum):
                #bypass the below and keep hitting card
                continue

            #if the dealer wins
            elif(player_sum<dealer_sum<=21):
                #player lose bet_money
                bank_roll.lose(money_bet)

                # if player lose money_bet and bank is empty, player lose, the game is over
                if bank_roll.amount == 0:
                    #break the  "hit or stay turn for player"
                    print("Your bank is 0, you lose, game over!!!!!")
                    play_on = False #break the hit or stay turn
                    break

                #if lose but still have money in bank
                print(f"Player lose, you have {bank_roll.amount} in bank")
                enter_4 = (input("Do you want to bet again?: yes/no")).lower()

                #break the hit or stay turn for dealer and play again
                if enter_4 == "yes":
                    play_again = True
                    play_on = False #break the hit or stay turn
                    break

                # break the hit or stay turn for dealer and end the game
                elif enter_4 == "no":
                    play_again = False
                    play_on = False #break the hit or stay turn
                    break

            #if player win
            elif(dealer_sum>21):
                bank_roll.win(money_bet)
                print(f"Player win, you have {bank_roll.amount} in bank")
                enter_3 = (input("Do you want to bet again? yes/no: ")).lower()

                # break the hit or stay turn for dealer and play again
                if enter_3 == "yes":
                    play_gain = True
                    play_on = False  # break the hit or stay turn
                    break

                # break the hit or stay turn for dealer and end the game
                elif enter_3 == "no":
                    play_again = False
                    play_on = False  # break the hit or stay turn
                    break


    if bank_roll.amount == 0:
        break
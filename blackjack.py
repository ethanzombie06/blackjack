import random

def add_card(deck,hand,ammount):
    for i in range(ammount):
        index = random.randint(0,len(deck)-1)
        hand.append(deck[index])
        deck.remove(deck[index])

def hand_val(hand):
    value = 0
    for i in hand:
        value += int(i[:len(i)-1])
    return(value)

def board(dealer,player):
    print("Dealer hand = ",dealer[0])
    print("Player hand = ",player,"\ncard value = ", hand_val(player))

def dealer_ai(hand):
    if hand_val(hand) > 21:
        return("dealer lost")

    elif hand_val(hand)<= 16:
        print("dealer hit")
        add_card(deck,hand,1)
        print("Dealer hand =",hand )
    else:
        print("dealer hand value = ",hand_val(hand))
        return(hand)
option = "y"
while option == "y":
    deck = ["1s","2s","3s","4s","5s","6s","7s","8s","9s","10s","10s","10s","10s"
            ,"1c","2c","3c","4c","5c","6c","7c","8c","9c","10c","10c","10c","10c"
            ,"1h","2h","3h","4h","5h","6h","7h","8h","9h","10h","10h","10h","10h"
            ,"1d","2d","3d","4d","5d","6d","7d","8d","9d","10d","10d","10d","10d"]
    dealer = []
    player = []

    add_card(deck,dealer,2)
    add_card(deck,player,2)

    while True:
        board(dealer,player)

        if hand_val(player) > 21:
                print("you lost!")
                break

        option = input("hit or stand?(h/s): ")

        if option == "h":
            add_card(deck,player,1)

        elif option == "s":
            dealer_val=dealer_ai(dealer)
            print("Dealer hand = ",dealer,"\ncard value = ", hand_val(dealer))

            if hand_val(dealer_val) > 21:
                print("dealer lost \nYou Win!")
            elif hand_val(player)<hand_val(dealer_val):
                print("you lost!")
                exit()
            else:
                print("you win!")
                exit()
        else:
            pass
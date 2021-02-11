from random import shuffle
import os

def clear_screen():
  _ = os.system("clear")

def create_deck():
  suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
  cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
  values = ["varies", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  deck = []
  for suit in suits:
    for i in range(len(cards)):
      deck.append([cards[i], suit, values[i]])

  shuffle(deck)
  return deck

def determine_score(player):

  scores = []

  num_aces = 0
  for card in player:
    if card[0] == "Ace":
      num_aces += 1
  
  if num_aces == 0:
    scores.append(0)
    for card in player:
      scores[0] += card[2]
  
  elif num_aces == 1:
    for case in range(2):
      scores.append(0)
      for card in player:
        try:
          scores[case] += card[2]
        except:
          if case == 0:
            scores[case] += 11
          else:
            scores[case] += 1

  else:
    scores.append(0)
    ace_value = 11
    for card in player:
      try:
        scores[0] += card[2]
      except:
        scores[0] += ace_value
        ace_value = 1
  
  return scores

def hand(deck):

  global player
  global dealer

  player = []
  dealer = []
  dealer_blackjack = False
  
  for i in range(2):

    player.append(deck[0])
    deck.pop(0)

    dealer.append(deck[0])
    deck.pop(0)

  player_scores = determine_score(player)
  dealer_scores = determine_score(dealer)

  for score in dealer_scores:
    if score == 21:
      dealer_blackjack = True

  for score in player_scores:
    if score == 21 and dealer_blackjack is not True:
      print("Blackjack! You win 1.5x Bet")
      game_over = True
      turn_over = True
      break
    elif score == 21 and dealer_blackjack is True:
      print("You both have blackjack, push")
      game_over = True
      turn_over = True
      break
    elif dealer_blackjack is True and score != 21:
      print("Dealer has blackjack, you lose")
      game_over = True
      turn_over = True
      break
    else:
      game_over = False
      turn_over = False
    
  print("Player has", player)
  print("Possible scores are:", player_scores)
  print("Dealer has", dealer[0], "showing")

  while turn_over is False:
    user_choice = input("Stand (s), Hit (h), Double Down (d): ")
    clear_screen()
    if user_choice in ["s", "S"]:
      turn_over = True
    
    elif user_choice in ["h", "H"]:
      player.append(deck[0])
      deck.pop(0)
      player_scores = determine_score(player)
      all_bust = True
      for score in player_scores:
        if score < 21:
          all_bust = False
        elif score == 21:
          print("You have 21!, let's see the dealer's hand")
          all_bust = False
          game_over = False
          turn_over = True
          break
        else:
          pass
      
      if all_bust is True:
        print("Bust! You lose")
        print("You had", player, "\n", player_scores)
        print("Dealer had", dealer_scores)
        game_over = True
        turn_over = True
      else:
        print("Player has", player)
        print("Possible scores are:", player_scores)
        print("Dealer has", dealer[0], "showing")

  dealer_best = 0
  dealer_bust = False
  for score in dealer_scores:
    if score > dealer_best and score <= 21:
      dealer_best = score
  
  while dealer_best < 17 and dealer_bust is False and game_over is False:
    print("Dealer has ", dealer_best, ", drawing...", sep="")
    dealer.append(deck[0])
    deck.pop(0)
    dealer_scores = determine_score(dealer)

    dealer_bust = True
    for score in dealer_scores:
      if score > dealer_best and score <= 21:
        dealer_best = score
        dealer_bust = False

  player_best = 0
  for score in player_scores:
    if score > player_best and score <= 21:
      player_best = score
  
  
  if player_best > dealer_best:
    print("Player wins!")
    print("You had:", player, "\n", player_best)
    print("Dealer had:", dealer, "\n", dealer_best)
  elif player_best < dealer_best:
    print("Player loses...")
    print("You had:", player, "\n", player_best)
    print("Dealer had:", dealer, "\n", dealer_best)
  else:
    print("Push, no winner")
    print("You had:", player, "\n", player_best)
    print("Dealer had:", dealer, "\n", dealer_best)

# Code to run game
clear_screen()

deck = create_deck()

hand(deck)

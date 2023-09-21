from art import logo, vs
from game_data import data
from replit import clear
import random


def get_people():
  copy_list = data
  key = random.randint(0,len(copy_list)-1)
  dict_person1 = copy_list[key]
  del copy_list[key]
  key2 = random.randint(0,len(copy_list)-1)
  dict_person2 = copy_list[key2]
  
  return dict_person1,dict_person2

def higher(person1,person2,guess):
  person1["name"].lower()
  person2["name"].lower()
  
  if guess == "a" and person1["follower_count"] > person2["follower_count"]:
    return 1
  elif guess == "b" and person2["follower_count"] > person1["follower_count"]:
    return 1
  else:
    return -1

def printer(a):
  #clear()
  print(f"You score is {a}")
  print(logo)
  person1,person2 = get_people()
  print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']} ")
  print(vs)
  print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}")
  return person1,person2
  
def play_game():
  score = 0
  clear()
  print(logo)
  person1,person2 = get_people()
  print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']} ")
  print(vs)
  print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}")

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  while higher(person1,person2,guess) >= 0:
    clear()
    score = score + higher(person1,person2,guess)
    printer(score)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
  print(f"Wrong, final score was {score}")
  play_again = input("Would you like to play again? 'y' or 'n': ").lower()
  if play_again == "y":
    play_game()
  else:
    print("Thanks for playing")


play_game()

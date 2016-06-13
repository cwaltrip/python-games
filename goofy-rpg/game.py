import sys

from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
  def setup(self):
    self.player = Character()
    self.monsters = [
      Goblin(),
      Troll(),
      Dragon()
    ]
    self.monster = self.get_next_monster()
    # print("Get ready!")
    
  def get_next_monster(self):
    try:
      return self.monsters.pop(0)
    except IndexError:
      return None
    
  def monster_turn(self):
    if self.monster.attack():
      print("The {} attacks! \"{}!\"".format(self.monster.name, self.monster.battlecry()))
      damage = self.monster.damage()
      if input("Dodge [Y/N]? ").lower() == 'y':
        if self.player.dodge():
          print("You expertly dodge the {}'s attack.".format(self.monster.name))
        else:
          print("You fail to dodge and take {} damage.".format(damage))
          self.player.hit_points -= damage
      else:
        print("You're hit for {} damage.".format(damage))
        self.player.hit_points -= damage
    else:
      print("The {} isn't attacking this turn.".format(self.monster.name))
    
  def player_turn(self):
    action = input("[A]ttack, [R]est, or [Q]uit? ").lower()
    if action == 'a':
      if self.player.attack():
        damage = self.player.damage()
        if self.monster.dodge():
          print("The {} evades your attack!".format(self.monster.name))
        else:
          print("You hit the {} with your {} for {} damage.".format(self.monster.name, self.player.weapon, damage))
          self.monster.hit_points -= damage
      else:
        print("Your attack misses the {}!".format(self.monster.name))
    elif action == 'r':
        self.player.rest()
    elif action == 'q':
        sys.exit()
    else:
      self.player_turn()
    
  def cleanup(self):
    if self.monster.hit_points < 1:
      self.player.experience += self.monster.experience
      print("You've defeated the {} and gained {} experience.".format(self.monster.name, self.monster.experience))
      self.monster = self.get_next_monster()
      
  def __init__(self):
    self.setup()
    
    while self.player.hit_points and (self.monster or self.monsters):
      # print("\n")
      print("{} is fighting a {}.\n".format(self.player, self.monster))
      self.monster_turn()
      # print("-"*20)
      self.player_turn()
      self.cleanup()
      # print("\n"+"="*20)
    
    print("\n")  
    if self.player.hit_points:
      print("You win!")
    elif self.monsters or self.monster:
      print("You lose!")
    sys.exit()

Game()

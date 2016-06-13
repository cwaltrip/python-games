import random

from combat import Combat

# Character: defines attributes and behavior for the player
class Character(Combat):

  # Define base and max values
  attack_limit = 10
  experience = 0
  base_hit_points = 10
  
  # Attack
  def attack(self):
    roll = random.randint(1, self.attack_limit)
    if self.weapon == 'sword':
      roll += 1
    elif self.weapon == 'axe':
      roll += 2
    return roll > 4
  
  # Get weapon choice
  def get_weapon(self):
    weapon_choice = input("Choose your weapon! ([S]word, [A]xe, [B]ow): ").lower()
    
    if weapon_choice in 'sab':
      if weapon_choice == 's':
        self.max_damage = 3
        return 'sword'
      elif weapon_choice == 'a':
        self.max_damage = 2
        return 'axe'
      else:
        self.max_damage = 2
        return 'bow'
    else:
      return self.get_weapon()

  # Init
  def __init__(self, **kwargs):
    self.name = input("What is your name, hero? ")
    self.weapon = self.get_weapon()
    self.hit_points = self.base_hit_points
    
    for key, value in kwargs.items():
      setattr(self, key, value)
  
  # String value    
  def __str__(self):
    return '{} (HP: {}, XP: {})'.format(self.name, self.hit_points, self.experience)
  
  # Rest
  def rest(self):
    if self.hit_points < self.base_hit_points:
      self.hit_points += 1
      print("You rest and regain health.")
    else:
      print("No need for your rest! You have full hit points.")
  
  # Level increase    
  def leveled_up(self):
    return self.experience >= 5


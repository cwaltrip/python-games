import random

# Combat: defines generic combat actions for monster and player
class Combat:

  # Define max values
  dodge_limit = 6
  attack_limit = 6
  max_damage = 3
  
  # Dodge
  def dodge(self):
    roll = random.randint(1, self.dodge_limit)
    return roll > 4
  
  # Attack
  def attack(self):
    roll = random.randint(1, self.attack_limit)
    return roll > 2

  # Get damage
  def damage(self):
  	return random.randint(1, self.max_damage)

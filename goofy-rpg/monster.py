import random

from combat import Combat

COLORS = ['yellow', 'red', 'blue', 'green']


class Monster(Combat):
  min_hit_points = 1
  max_hit_points = 1
  min_experience = 1
  max_experience = 1
  weapon = 'sword'
  sound = 'roar'
  
  def __init__(self, **kwargs):
    self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
    self.experience = random.randint(self.min_experience, self.max_experience)
    self.color = random.choice(COLORS)
    self.name = '{} {}'.format(self.color.title(), self.__class__.__name__)
    
    for key, value in kwargs.items():
      setattr(self, key, value)
      
  def __str__(self):
    return '{} (HP: {}, XP: {})'.format(self.name, self.hit_points, self.experience)
  
  def battlecry(self):
    return self.sound.upper()
  
  
class Goblin(Monster):
  max_hit_points = 3
  max_experience = 2
  max_damage = 2
  sound = 'squeak'

  
class Troll(Monster):
  min_hit_points = 3
  max_hit_points = 5
  min_experience = 2
  max_experience = 6
  max_damage = 4
  sound = 'growl'
  
  
class Dragon(Monster):
  min_hit_points = 5
  max_hit_points = 10
  min_experience = 6
  max_experience = 10
  max_damage = 8
  sound = 'raaaaaaaaaaar'
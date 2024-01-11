class Car:
  def __init__(self, speed, color='Yellow', owner='None'):
    self.speed= speed
    self.color= color 
    self.owner= owner

  def say_owner(self):
    if self.owner:
      print(f'Vladelets{self.owner}')
    else:
      print('U dannogo avto net vladeltsa')

car1 = Car(speed=100, owner='Ivan')
car2 = Car(80, 'Green')
car1.say_owner()
car2.say_owner()
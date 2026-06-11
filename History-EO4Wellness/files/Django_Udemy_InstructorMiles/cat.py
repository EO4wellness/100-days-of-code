class Cat():

  color = 'black'

  def __init__(self, color):
    self.color = color

  def sound(self, sound):
    print self.color

  def set_color(self, color):
    self.color

tom_the_cat = Cat('brown')
tom_the_cat.sound('puuurrrrr')

spot_the_cat = Cat('black')
spot_the_cat.sound('hiss')
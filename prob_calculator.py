import random
import copy

# create class Hat
class Hat:
  def __init__(self, **kwargs):
    self.array = []
    self.contents = []
    self.array.append(kwargs)
    for x in self.array[0]:
      number_color = self.array[0][x]
      for num in range(number_color):
        self.contents.append(x)
  
  def __repr__(self):    
    return str(self.contents)
  
  def draw(self, number_of_balls):
    total_number_of_ball = len(self.contents)
    if total_number_of_ball < number_of_balls:
      return self.contents

    removed_balls = []
    for num in range(int(number_of_balls)):
      random_element = random.choice(self.contents)
      removed_balls.append(random_element)
      self.contents.remove(random_element)
    return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  for x in range(num_experiments):
    
    #deepcopy the hat everytime so that each experiment will be new
    hat_given = copy.deepcopy(hat)
    succeeded = True
    result_of_one_exp = hat_given.draw(num_balls_drawn)
    for x in expected_balls:
      number_of_expected_balls = expected_balls[x]
      number_of_actual_balls = result_of_one_exp.count(x)
      if number_of_expected_balls > number_of_actual_balls:
        succeeded = False
    
    if succeeded == True:
      success += 1
  
  probabiliy = success / num_experiments
  return probabiliy

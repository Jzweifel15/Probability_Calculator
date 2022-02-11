import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **colors):
    self.contents = []
    for key, value in colors.items():
      for _ in range(value):
        self.contents.append(key)

  def draw(self, num_of_draws):
    if num_of_draws <= len(self.contents):
      balls_drawn = []
      for _ in range(num_of_draws):
        rand_num = random.randrange(len(self.contents))
        balls_drawn.append(self.contents[rand_num])
        self.contents.pop(rand_num)  
      return balls_drawn
    else:
      return self.contents
      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected = []
  for key, value in expected_balls.items():
    for _ in range(value):
      expected.append(key)

  M = 0
  contents_copy = copy.deepcopy(hat.contents)

  for _ in range(num_experiments):
    balls_drawn = hat.draw(num_balls_drawn)
    hat.contents = copy.deepcopy(contents_copy)

    count = 0
    for i in expected:
      for j in balls_drawn:
        if i == j:
          count += 1
          balls_drawn.pop(balls_drawn.index(j))
          break
      if count == len(expected):
        M += 1

  return M / num_experiments
import string
import random

class Dice:
  def __init__(self):
    self._dice = []
    for i in range(6):
      self._dice.append(random.choice(string.ascii_letters).upper())
  

class BoggleBoard:

  def __init__(self):
    self._board = []

    for i in range(4):
      entry = ['-','-','-','-']
      self._board.append(entry)

  def __str__(self):
    return f"{self._board}"
  
  def __str__(self):
    ret = ""
    for i in range(4):
        for j in range(4):
            ret += self._board[i][j]

        ret += '\n'
    return ret

  def shake(self):
    for i in range(4):
      for j in range(4):
        new_dice = Dice()
        roll = random.choice(new_dice._dice)
        self._board[i][j] = roll
        if(self._board[i][j] == 'Q'):
          self._board[i][j] = 'Qu '
        else:
          self._board[i][j] += '  '
        

new_dice = Dice()
print(new_dice._dice)

bboard = BoggleBoard()
print(bboard)

bboard.shake()
print(bboard)



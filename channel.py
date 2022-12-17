from columns import Columns

class Channel(Columns):
  def __init__(self):
    super().__init__()
    self._data = [' ', ' ', ' ', ' ', ' ', ' ']

  def execute(self):
    #returns data
    return self._data

  def makePlay(self, player):
    #takes in player that made the play, and then adds their token if there is space left
    if self._data[0] != 'O' and self._data[0] != 'X':
      if player == 1:
        symbol = 'X'
      else:
        symbol = 'O'

      i = len(self._data) - 1

      while i >= 0:
        if self._data[i] == ' ':
          self._data[i] = symbol
          return i + 1
        
        i -= 1

    else:
      return False
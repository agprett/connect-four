from columns import Columns

class Walls(Columns):
  def __init__(self):
    super().__init__()
    self._data = ['|', '|', '|', '|', '|', '|']

  def execute(self):
    #returns the list to be used by game
    return self._data
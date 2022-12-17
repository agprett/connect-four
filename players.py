class Players:
  def __init__(self):
    self._plays = []

  def addPlay(self, coord):
    #adds the coordinate provided to the players list of plays
    self._plays.append(coord)

  def checkPlays(self, coord):
    #checks to see if a coordinate is present in the users plays
    if coord in self._plays:
      return True
    else:
      return False
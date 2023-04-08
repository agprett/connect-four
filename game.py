class Game:
  def __init__(self):
    self._turn = 0
    self._divider = '+ - + - + - + - + - + - + - +'

  def displayBoard(self, walls, columns):
    #this takes in the walls to display, then columns to show where is open and what has been played
    viewedColumns = {}
    print('  1   2   3   4   5   6   7')

    for column in columns:
      viewedColumns[column] = columns[column].execute()

    for i in range(6):
      line = f"{walls[i]} {viewedColumns['column1'][i]} {walls[i]} {viewedColumns['column2'][i]} {walls[i]} {viewedColumns['column3'][i]} {walls[i]} {viewedColumns['column4'][i]} {walls[i]} {viewedColumns['column5'][i]} {walls[i]} {viewedColumns['column6'][i]} {walls[i]} {viewedColumns['column7'][i]} {walls[i]}"

      print(line)
      print(self._divider)
    
    print('')

  def takeTurn(self, column):
    #attempts to make a play, if it can't it will alert the user
    attempt = column.makePlay(self._turn + 1)

    if attempt:
      if self._turn == 0:
        self._turn = 1
      else:
        self._turn = 0
      
      return attempt

    else:
      print('This stack is full, try again.')
      return False

  def checkWin(self, player, coord):
    #takes in the player who made a move and the coordinate of their play, then checks to see if that wins them the game
    winCount = 1
    checkX = coord[0]
    checkY = coord[1]
    print(coord)

    #checks win down
    while True:
      checkY += 1
      played = player.checkPlays([checkX, checkY])

      if checkY > 6 or played == False:
        winCount = 1
        checkX = coord[0]
        checkY = coord[1]
        break
      else:
        winCount += 1

      if winCount >= 4:
        return True

    #checks left to get how many player has left of the play
    while True:
      checkX -= 1
      played = player.checkPlays([checkX, checkY])

      if checkX < 1 or played == False:
        checkX = coord[0]
        checkY = coord[1]
        break
      else:
        winCount += 1

      if winCount >= 4:
        return True

    #check right to see if player wins with that play
    while True:
      checkX += 1
      played = player.checkPlays([checkX, checkY])

      if checkX > 7 or played == False:
        winCount = 1
        checkX = coord[0]
        checkY = coord[1]
        break
      else:
        winCount += 1

      if winCount >= 4:
        return True

    # check down left for win
    while True:
      checkX -= 1
      checkY -= 1
      played = player.checkPlays([checkX, checkY])

      if checkX < 1 or checkY > 6 or played == False:
        checkX = coord[0]
        checkY = coord[1]
        break
      else:
        winCount += 1

      if winCount >= 4:
        return True

    #checks up right for win
    while True:
      checkX += 1
      checkY += 1
      played = player.checkPlays([checkX, checkY])

      if checkX > 7 or checkY < 1 or played == False:
        winCount = 1
        checkX = coord[0]
        checkY = coord[1]
        break
      else:
        winCount += 1

      if winCount >= 4:
        return True

    #check up left for win
    while True:
      checkX -= 1
      checkY += 1
      played = player.checkPlays([checkX, checkY])

      if checkX < 1 or checkY < 1 or played == False:
        checkX = coord[0]
        checkY = coord[1]
        break
      else:
        winCount += 1

      if winCount >= 4:
        return True

    #checks down right for win
    while True:
      checkX += 1
      checkY -= 1
      played = player.checkPlays([checkX, checkY])

      if checkX > 7 or checkY < 6 or played == False:
        winCount = 1
        checkX = coord[0]
        checkY = coord[1]
        break
      else:
        winCount += 1

      if winCount >= 4:
        return True

    #this will return false if in no way does the player win with the play made
    return False

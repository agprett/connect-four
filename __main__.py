from game import Game
from walls import Walls
from channel import Channel
from players import Players

def main():
  game = Game()

  wall = Walls()

  column1 = Channel()
  column2 = Channel()
  column3 = Channel()
  column4 = Channel()
  column5 = Channel()
  column6 = Channel()
  column7 = Channel()

  player1 = Players()
  player2 = Players()

  print('Welcome to Connet 4!')
  
  columns = {
    'column1': column1,
    'column2': column2,
    'column3': column3,
    'column4': column4,
    'column5': column5,
    'column6': column6,
    'column7': column7
  }

  game.displayBoard(wall.execute(), columns)

  turn = 'Player 1'

  while True:
    slot = input(f'{turn}, Choose a slot to drop your tile (1-7): ')

    attempt = game.takeTurn(columns[f'column{slot}'])

    if attempt:
      playedCoord = [int(slot), attempt]
      if turn == 'Player 1':
        player1.addPlay(playedCoord)
        win = game.checkWin(player1, playedCoord)
        # win = False
        if win:
          game.displayBoard(wall.execute(), columns)
          print(f'{turn} wins!')
          break
        else:
          turn = 'Player 2'
      else:
        player2.addPlay(playedCoord)
        win = game.checkWin(player2, playedCoord)
        # win = False
        if win:
          game.displayBoard(wall.execute(), columns)
          print(f'{turn} wins!')
          break
        else:
          turn = 'Player 1'

    print('')
    game.displayBoard(wall.execute(), columns)
    print('')

if __name__ == "__main__":
  main()
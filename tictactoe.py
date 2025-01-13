import re

class TicTacToe:
    
    def __init__(self):
        self.board = None
        self.turn = "X"
        self.is_placed = None

    def create_empty_board(self):
        self.board = [
            ['A', 'B', 'C'],
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-'],
        ]

    def place_o_x(self, position, turn):

        if turn == "X":
          mark = "x"
        elif turn == "O":
          mark = "o"
        
        position = position.upper()
        row = re.findall(r'\d+', position)
        col = re.findall(r'^\S', position)
        col_map = list(zip(self.board[0], [1, 2, 3]))
        col_num = None
        row_num = int(row[0])
        for m in col_map:
          if col[0] == m[0]:
            col_num = int(m[1])
          else:
             pass
        
        if self.board[row_num][col_num - 1] == '-':
          self.board[row_num][col_num - 1] = mark
          self.is_placed = True
        else:
          self.is_placed = False

    def resolve_board_state(self):
        pass

    def print_board(self):
        board = self.board
        header = "   {0}  {1}  {2}".format(board[0][0], board[0][1], board[0][2])
        print(header)
        for i, row in enumerate(board[1:]):
            out = "{0}  {1}  {2}  {3}".format(i+1, row[0], row[1], row[2])
            print(out)

def main():
    ttt = TicTacToe()
    ttt.create_empty_board()
    while True:
      ttt.print_board()
      print('\n')
      if ttt.turn == "X":
        position = input("Enter new X positino (ex. A1): ")
        print('\n')
        ttt.place_o_x(position, ttt.turn)
        if ttt.is_placed == True:
           ttt.turn = "O"
      elif ttt.turn == "O":
        position = input("Enter new O positino (ex. B2): ")
        print('\n')
        ttt.place_o_x(position, ttt.turn)
        if ttt.is_placed == True:
           ttt.turn = "X"

if __name__ == "__main__":
    main()

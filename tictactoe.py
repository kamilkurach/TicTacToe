import re

class TicTacToe:
    
    def __init__(self):
        self.board = None
        self.turn = "X"
        self.is_placed = None
        self.is_X_win = None
        self.is_O_win = None

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
        self.check_rows()
        self.check_cols()
        self.check_diag()

    def check_rows(self):
        board = self.board[1:]
        for row in board:
           if row.count('x') == 3:
              print("X won!")
              self.is_X_win = True
           elif row.count('o') == 3:
              print("O won!")
              self.is_O_win = True

    def check_cols(self):
        board = self.board[1:]
        for i in range(3):
           tmp = []
           for row in board:
              tmp.append(row[i])
           if tmp.count('x') == 3:
              print("X won!")
              self.is_X_win = True
           elif tmp.count('o') == 3:
              print("O won!")
              self.is_O_win = True

    def check_diag(self):
        board = self.board[1:]
        tmp = []
        for i, row in enumerate(board):
            tmp.append(row[i])
        if tmp.count('x') == 3:
            print("X won!")
            self.is_X_win = True
        elif tmp.count('o') == 3:
            print("O won!")
            self.is_O_win = True
       
        tmp = []
        for i, row in enumerate(board):
            tmp.append(row[len(board) - 1 - i])
        if tmp.count('x') == 3:
            print("X won!")
            self.is_X_win = True
        elif tmp.count('o') == 3:
            print("O won!")
            self.is_O_win = True

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
        position = input("Enter new X (ex. A1): ")
        print('\n')
        ttt.place_o_x(position, ttt.turn)
        if ttt.is_placed == True:
           ttt.turn = "O"
      elif ttt.turn == "O":
        position = input("Enter new O (ex. B2): ")
        print('\n')
        ttt.place_o_x(position, ttt.turn)
        if ttt.is_placed == True:
           ttt.turn = "X"
      
      ttt.resolve_board_state()
      
      if ttt.is_O_win is True or ttt.is_X_win is True:
         ttt.print_board()
         break

if __name__ == "__main__":
    main()

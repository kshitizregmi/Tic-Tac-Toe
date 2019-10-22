import os
import time
# clear = lambda : os.system('cls')

class tictactoe:
    def __init__(self):
        self.board =["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

    def display_board(self):
        print("\t\t\t TIC TAC TOE GAME !!!\n")
        print("\n")
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2] + "     1 | 2 | 3")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5] + "     4 | 5 | 6")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8] + "     7 | 8 | 9")
        print("\n")

    def firstchoose(self):
        print("Choose Your Symbol :")
        # Tells us who the current player is
        cp = input("X or O : ")
        current_player = "X" if cp=="x"or cp=='X' else "O"
        return current_player

    def clear(self):
        return os.system('cls')

    def move(self,current_player):
        userinput=0
        print("Player {} Enter your move : ".format(current_player) )
        try:
            userinput = int(input("Enter number between 1 to 9 : "))
        except ValueError as v:
            print("Value error " + str(v))
            time.sleep(3)
            self.clear()
            self.display_board()
            self.move(current_player)

        if userinput <= 9 and userinput >= 1:
            if self.board[userinput-1] == "-":
                self.board[userinput-1]= current_player
                self.check_winner(self.board, current_player)
                #change player turn
                if current_player=="X":
                    current_player="O"
                else:
                    current_player="X"
                # change current player and dispaly board
                self.clear()
                self.display_board()
                #move for new player
                self.move(current_player)

        else:
            print("Invalid input press any key to try again!! or press n button to exit")
            exit_val = input()
            if exit_val == "n" or exit_val== "N":
                self.clear()
                self.display_board()
                exit("Program Exit")
            else:
                self.clear()
                self.display_board()
                self.move(current_player)


    def check_winner(self ,board, player):
        # If any row does have a match, flag that there is a win
        row_1 = self.board[0] == self.board[1] == self.board[2] != "-"
        row_2 = self.board[3] == self.board[4] == self.board[5] != "-"
        row_3 = self.board[6] == self.board[7] == self.board[8] != "-"
        # If any col does have a match, flag that there is a win
        col_1 = self.board[0] == self.board[3] == self.board[6] != "-"
        col_2 = self.board[1] == self.board[4] == self.board[7] != "-"
        col_3 = self.board[2] == self.board[5] == self.board[8] != "-"
        #check diagonal
        di_1 = self.board[0] == self.board[4] == self.board[8] != "-"
        di_2 = self.board[2] == self.board[4] == self.board[6] != "-"

        if row_1== True or row_2== True or row_3== True:
            self.clear()
            self.display_board()
            print("Winner is Player {} !!".format(player))
            time.sleep(5)
            self.restart()

        elif col_1== True or col_2== True or col_3== True:
            self.clear()
            self.display_board()
            print("Winner is Player {} !!".format(player))
            time.sleep(3)
            self.restart()

        elif di_1==True or di_2==True:
            self.clear()
            self.display_board()
            print("Winner is Player {} !!".format(player))
            time.sleep(3)
            self.restart()
        
        elif '-' in board :
            pass
        else:
            # print("Game Tied")
            self.clear()
            self.display_board()
            print("Game Tied")
            time.sleep(5)
            self.restart()

    def restart(self):
        print("Do you want to continue [Y/N]: ")
        continue_value = input()
        if continue_value == 'y' or continue_value=='Y':
            self.__init__()
            self.display_board()
            ch = self.firstchoose()
            self.move(ch)
        else:
            exit()

if __name__ == "__main__":
    tic = tictactoe()
    tic.display_board()
    currentplayer = tic.firstchoose()
    tic.move(currentplayer)


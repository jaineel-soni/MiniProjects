def sum(a,b,c):
    return a+b+c
def PrintBoard(Xstate,Ystate):
    zero = 'X' if Xstate[0] else ('O' if Ystate[0] else 0)
    one = 'X' if Xstate[1] else ('O' if Ystate[1] else 1)
    two = 'X' if Xstate[2] else ('O' if Ystate[2] else 2)
    three = 'X' if Xstate[3] else ('O' if Ystate[3] else 3)
    four = 'X' if Xstate[4] else ('O' if Ystate[4] else 4)
    five = 'X' if Xstate[5] else ('O' if Ystate[5] else 5)
    six = 'X' if Xstate[6] else ('O' if Ystate[6] else 6)
    seven = 'X' if Xstate[7] else ('O' if Ystate[7] else 7)
    eight = 'X' if Xstate[8] else ('O' if Ystate[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
def checkwin(Xstate,Ystate):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(Xstate[win[0]],Xstate[win[1]],Xstate[win[2]])==3):
            print("X won the match")
            return 1 
        if (sum(Ystate[win[0]],Ystate[win[1]],Ystate[win[2]])==3):
            print("0 won the match")
            return 0
    return -1    

Xstate = [0,0,0,0,0,0,0,0,0]
Ystate = [0,0,0,0,0,0,0,0,0]
turn = 1 # 1 for X and 0 for O

print("Welcome to the tic-tac-toe game !!!")
while True:
    
    if turn == 1:
        print("X's turn")
        value = int(input("please enter a value"))
        Xstate[value] = 1
        PrintBoard(Xstate,Ystate)    
    else:
        print("O's turn")
        value = int(input("please enter a value"))
        Ystate[value] = 1
        PrintBoard(Xstate,Ystate)
    cwin = checkwin(Xstate,Ystate)
    
    if cwin != -1:
        print("Match over!!")
        break
        
    
    turn = 1 - turn
    
        
    

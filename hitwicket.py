print("WELCOME TO THE CHESS GAME")

# Input name of first player
player1=input("Enter the name of player 1: ")

# Input name of second player
player2=input("Enter the name of player 2: ")

#chess board
board=[]
for i in range(5):
    l=["XXX"]*5
    board.append(l)

# Player 1 pawns
# For player 1 use P1,P2,P3,P4,P5
print("Initial locations of pawns of Player 1")
player1_inital_arrangements=input().split(",")
for i in player1_inital_arrangements:
    x=i[-1]
    board[0][int(x)-1]=player1+i[0:2]


# Player 2 pawns
# For player 1 use p1,p2,p3,p4,p5
print("Initial locations of pawns of Player 2")
player2_inital_arrangements=input().split(",")
for i in player2_inital_arrangements:
    x=i[-1]
    board[4][int(x)-1]=player2+i[0:2]

print(board)



print("Let's Start the game")

killed_player1=[]
killed_player2=[]

c=1
while True:
    if c%2==1:
        player1_move=input("Player's 1 move: ")
        for i in range(5):
            flag=False
            for j in range(5):
                if board[i][j][-2]+board[i][j][-1]==player1_move[:2]:
                    if player1_move[-1]=="F":
                        if i+1>4:
                            print("Invalid Input")
                            flag=True
                            break
                        elif player1 in board[i+1][j]:
                            print("Can't kill own player")
                            flag=True
                            break
                        elif player2 in board[i+1][j]:
                            killed_player2.append(board[i+1][j][-2]+board[i+1][j][-1])
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i+1][j]=y
                            c=c+1
                            flag=True
                            break
                        else:
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i+1][j]=y
                            c=c+1
                            flag=True
                            break
                    if player1_move[-1]=="B":
                        if i-1<0:
                            print("Invalid Input")
                            flag=True
                            break
                        elif player1 in board[i-1][j]:
                            print("Can't kill own player")
                            flag=True
                            break
                        elif player2 in board[i-1][j]:
                            killed_player2.append(board[i-1][j][-2]+board[i-1][j][-1])
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i-1][j]=y
                            c=c+1
                            flag=True
                            break
                        else:
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i-1][j]=y
                            c=c+1
                            flag=True
                            break
                    if player1_move[-1]=="R":
                        if j+1>4:
                            print("Invalid Input")
                            flag=True
                            break
                        elif player1 in board[i][j+1]:
                            print("Can't kill own player")
                            flag=True
                            break
                        elif player2 in board[i][j+1]:
                            killed_player2.append(board[i][j+1][-2]+board[i][j+1][-1])
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i][j+1]=y
                            c=c+1
                            flag=True
                            break
                        else:
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i][j+1]=y
                            c=c+1
                            flag=True
                            break
                    if player1_move[-1]=="L":
                        if j-1<0:
                            print("Invalid Input")
                            flag=True
                            break
                        elif player1 in board[i][j-1]:
                            print("Can't kill own player")
                            flag=True
                            break
                        elif player2 in board[i][j-1]:
                            killed_player2.append(board[i][j-1][-2]+board[i][j-1][-1])
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i][j-1]=y
                            c=c+1
                            flag=True
                            break
                        else:
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i][j-1]=y
                            c=c+1
                            flag=True
                            break
            if flag==True:
                break
    elif c%2==0:
        player2_move=input("Player's 2 move: ")
        for i in range(len(board)):
            flag=False
            for j in range(len(board[i])):
                if board[i][j][-2]+board[i][j][-1]==player2_move[:2]:
                    if player2_move[-1]=="F":
                        if i+1>4:
                            print("Invalid Input")
                            flag=True
                            break
                        elif player2 in board[i+1][j]:
                            print("Can't kill own player")
                            flag=True
                            break
                        elif player1 in board[i+1][j]:
                            killed_player1.append(board[i+1][j][-2]+board[i+1][j][-1])
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i+1][j]=y
                            c=c+1
                            flag=True
                            break
                        else:
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i+1][j]=y
                            c=c+1
                            flag=True
                            break
                    if player2_move[-1]=="B":
                        if i-1<0:
                            print("Invalid Input")
                            flag=True
                            break
                        elif player2 in board[i-1][j]:
                            print("Can't kill own player")
                            flag=True
                            break
                        elif player1 in board[i-1][j]:
                            killed_player1.append(board[i-1][j][-2]+board[i-1][j][-1])
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i-1][j]=y
                            c=c+1
                            flag=True
                            break
                        else:
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i-1][j]=y
                            c=c+1
                            flag=True
                            break
                    if player2_move[-1]=="R":
                        if j+1>4:
                            print("Invalid Input")
                            flag=True
                            break
                        elif player2 in board[i][j+1]:
                            print("Can't kill own player")
                            flag=True
                            break
                        elif player1 in board[i][j+1]:
                            killed_player1.append(board[i][j+1][-2]+board[i][j+1][-1])
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i][j+1]=y
                            c=c+1
                            flag=True
                            break
                        else:
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i][j+1]=y
                            c=c+1
                            flag=True
                            break
                    if player2_move[-1]=="L":
                        if j-1<0:
                            print("Invalid Input")
                            flag=True
                            break
                        elif player2 in board[i][j-1]:
                            print("Can't kill own player")
                            flag=True
                            break
                        elif player1 in board[i][j-1]:
                            killed_player1.append(board[i][j-1][-2]+board[i][j-1][-1])
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i][j-1]=y
                            c=c+1
                            flag=True
                            break
                        else:
                            y=board[i][j]
                            board[i][j]="XXX"
                            board[i][j-1]=y
                            c=c+1
                            flag=True
                            break
            if flag==True:
                break
    print(board)
    print(killed_player1)
    print(killed_player2)
    if len(killed_player1)==5:
        print(player2+" "+"win")
        break
    if len(killed_player2)==5:
        print(player1+" "+"win")
        break
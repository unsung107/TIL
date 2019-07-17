import copy
for rounds in range(int(input())):
    
    N = int(input())
    
    goal_board = []
    for i in range(N):
        goal_board.append(list(input().split()))

    board_90 = []
    board_180 = []
    board_270 = []

    #90

    #180도회전
    board_180 = copy.deepcopy(goal_board)
    board_180.reverse()
    for i in range(N):
        board_180[i].reverse()

    

    print(board_180)
    print(goal_board)
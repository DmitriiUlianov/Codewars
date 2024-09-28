def is_solved(board):

    i = 0
    j = 0
    count1 = 0
    count2 = 0
    
    while i < 3:
        while j < 3:
            if board[i][j] == 1:
                count1 += 1
            if board[i][j] == 2:
                count2 += 1
            j += 1
        if count1 == 3:
            return 1
        if count2 == 3:
            return 2
        count1 = 0
        count2 = 0
        j = 0
        i += 1
        
    i = 0
    j = 0  
    while i < 3:
        while j < 3:
            if board[j][i] == 1:
                count1 += 1
            if board[j][i] == 2:
                count2 += 1
            j += 1
        if count1 == 3:
            return 1
        if count2 == 3:
            return 2
        count1 = 0
        count2 = 0
        j = 0
        i += 1
        
    if (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1):
        return 1
    if (board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 1):
        return 1
    if (board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2):
        return 2
    if (board[2][0] == 2 and board[1][1] == 2 and board[0][2] == 2):
        return 2
    
    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        return 0
    elif 0 in board[0] or 0 in board[1] or 0 in board[2]:
        return -1

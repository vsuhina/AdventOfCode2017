
def key(x,y):
    return "{0}.{1}".format(x,y)

def coords(x,y,move):
    if move == 'R':
        return x+1, y
    elif move == 'U':
        return x, y+1
    elif move == 'L':
        return x-1, y
    elif move == 'D':
        return x, y-1
    else:
        return x,y

def sum(x,y, dict):
    s = 0
    s += tryGetItem(x+1, y,   dict)
    s += tryGetItem(x+1, y+1, dict)
    s += tryGetItem(x,   y+1, dict)
    s += tryGetItem(x-1, y+1, dict)
    s += tryGetItem(x-1, y,   dict)
    s += tryGetItem(x-1, y-1, dict)
    s += tryGetItem(x,   y-1, dict)
    s += tryGetItem(x+1, y-1, dict)

    return s

def tryGetItem(x, y, dict):
    k = key(x,y);
    if dict.get(k) is not None:
        return dict[k]
    else:
        return 0

    
if __name__ == "__main__":

    input = 312051

    matrix_size = 20 # guess

    # directions - each move is represented with one letter: R - right, U - up, L - left, D - down
    directions = ['R' + ('U'*(i-1))[:-1] + 'L'*(i-1) + 'D'*(i-1) + 'R'*(i-1) for i in range(1,matrix_size,2)]

    # moves - all moves in one list
    moves = ''.join(directions[1:])

    x = 0
    y = 0

    val = 1

    dict = {}
    k = key(x,y)
    dict[k] = val

    for move in moves:
        x, y = coords(x,y, move)
        s = sum(x,y,dict)
        dict[key(x,y)] = s
        if (s > input):
            print(s)
            break


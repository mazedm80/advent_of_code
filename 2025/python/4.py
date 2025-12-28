def forklifts(i, j, rolls, already_accessed, p2):
    rolls_count = 0
    adj_pos = [(0,1), (0,-1), (1,0), (-1,0), (-1,1),(1,1),(1,-1),(-1,-1)]
    for i_adj, j_adj in adj_pos:
        i_dx = i+i_adj
        j_dx = j+j_adj
        if i_dx >= 0 and i_dx < len(rolls) and j_dx >= 0 and j_dx < len(rolls[0]):
            if not p2:
                if rolls[i_dx][j_dx] == '@':
                    rolls_count += 1
            else:
                if rolls[i_dx][j_dx] == '@' and (i_dx, j_dx) not in already_accessed:
                    rolls_count += 1
    if rolls_count < 4:
        return True
    else:
        return False


def main():
    with open("./input.txt") as f:
        lines = f.readlines()
    rolls = []
    for line in lines:
        rolls.append([i for i in line.strip()])
    
    already_accessed = set()
    result_1 = 0
    for i in range(len(rolls)):
        for j in range(len(rolls[0])):
            if rolls[i][j] == '@' and forklifts(i, j, rolls, already_accessed, False):
                result_1+=1

    removeable = True
    result_2 = 0
    while removeable:
        rolls_count = 0
        current_accessed = set()
        for i in range(len(rolls)):
            for j in range(len(rolls[0])):
                if (i, j) not in already_accessed and rolls[i][j] == '@' \
                    and forklifts(i, j, rolls, already_accessed, True):
                    rolls_count+=1
                    current_accessed.add((i, j))
        if rolls_count > 0:
            result_2+=rolls_count
            already_accessed.update(current_accessed)
        else:
            removeable = False
    
    print(f"part 1: {result_1}")
    print(f"part 2: {result_2}")


if __name__ == "__main__":
    main()
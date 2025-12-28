def check_invalid(num: str) -> bool:
    if len(num) % 2 != 0:
        return False
    mid = len(num) // 2
    if num[:mid] == num[mid:]:
        return True

def check_invalid_p2(num: str) -> bool:
    s = str(num)
    length = len(s)

    for block_len in range(1, length // 2 + 1):
        if length % block_len == 0:
            block = s[:block_len]
            if block * (length // block_len) == s:
                return True
    return False


def main():
    ids = []
    with open("./input.txt") as f:
        lines = f.readlines()
        for line in lines:
            tmp = line.split(',')
            for id in tmp:
                ids.append(tuple(id.split('-')))
    
    result_1 = 0
    result_2 = 0
    for id in ids:
        if not len(id[0]) > 1 and not len(id[1]) > 1:
            continue
        for num in range(int(id[0]), int(id[1])+1):
            if check_invalid(str(num)):
                result_1+=num
            if check_invalid_p2(str(num)):
                result_2+=num
    
    print(f"part 1: {result_1}")
    print(f"part 2: {result_2}")


if __name__ == "__main__":
    main()
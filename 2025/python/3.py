def find_jolt(bat: list, jol_len: int):
    jolt = ""   
    while(len(jolt) < jol_len):
        highest = max(bat[:len(bat) - jol_len + len(jolt) + 1])
        jolt+= str(highest)
        bat = bat[bat.index(highest) + 1:]
    return jolt


def main():
    with open("./input.txt") as f:
        lines = f.readlines()
        bats = [line.strip() for line in lines]
    
    result_1 = 0
    result_2 = 0
    for bat in bats:
        bat_c = [int(c) for c in bat]
        result_1 += int(find_jolt(bat_c, 2))
        result_2 += int(find_jolt(bat_c, 12))
    
    print(f"part 1: {result_1}")
    print(f"part 2: {result_2}")


if __name__ == "__main__":
    main()
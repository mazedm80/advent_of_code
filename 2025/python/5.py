def main():
    fresh_ids = []
    ids = []

    with open("./input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            if "-" in line:
                start, end = map(int, line.split("-"))
                fresh_ids.append((start, end))
            else:
                ids.append(int(line))
    
    result_1 = 0
    for id in ids:
        for start, end in fresh_ids:
            if id >= start and id <= end:
                result_1+=1
                break
    
    fresh_ing_ids = []
    fresh_ids.sort(key=lambda x: x[0])
    for start, end in fresh_ids:
        if not fresh_ing_ids or start > fresh_ing_ids[-1][1]:
            fresh_ing_ids.append([start, end])
        else:
            fresh_ing_ids[-1][1] = max(fresh_ing_ids[-1][1], end)
    result_2 = sum([(end - start)+1 for start, end in fresh_ing_ids])

    print(f"part 1: {result_1}")
    print(f"part 2: {result_2}")


if __name__ == "__main__":
    main()
from collections import defaultdict


def main():
    with open("./input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    beams = [defaultdict(lambda: 0) for _ in range(len(lines))]
    beams[0][lines[0].find('S')] = 1
    splits = set()
    for row in range(1, len(lines)):
        for col, val in beams[row-1].items():
            if lines[row][col] == '^':
                beams[row][col-1] = beams[row][col-1] + val
                beams[row][col+1] = beams[row][col+1] + val
                splits.add((col, row))
            else:
                beams[row][col] = beams[row][col] + val
    
    print(f"part 1: {len(splits)}")
    print(f"part 2: {sum(beams[-1].values())}")


if __name__ == "__main__":
    main()
import math


def get_input():
    problems = []
    nums = []
    with open("./input.txt") as f:
        lines = f.readlines()
        ops = lines[-1].strip().split()
        for line in lines[:-1]:
            line = line.strip()
            nums.append(line.split())
    for i in range(len(nums[0])):
        n = []
        for j in range(len(nums)):
            n.append(nums[j][i])
        problems.append(n)


    return problems, ops

def get_input_p2():
    hw = []
    with open("./input.txt") as f:
        lines = f.readlines()
        ops = lines[-1].strip().split()
        for line in lines[:-1]:
            hw.append([c for c in line])
    problems = []
    nums = []
    for i in range(len(hw[0])):
        row = len(hw)
        if all(hw[j][i] == ' ' for j in range(row)):
            problems.append(nums)
            nums = []
        else:
            tmp = "".join([hw[j][i] for j in range(row)]).strip()
            if tmp.isalnum():
                nums.append(tmp)
    problems.append(nums)
    return problems, ops


def main():
    problems, ops = get_input()
    result_1 = 0
    for i in range(len(ops)):
        if ops[i] == '+':
            result_1 += sum(map(int, problems[i]))
        else:
            result_1 += math.prod(map(int, problems[i]))

    problems, ops = get_input_p2()
    result_2 = 0
    for i in range(len(ops)):
        if ops[i] == '+':
            result_2 += sum(map(int, problems[i]))
        else:
            result_2 += math.prod(map(int, problems[i]))

    print(f"part 1: {result_1}")
    print(f"part 2: {result_2}")


if __name__ == "__main__":
    main()
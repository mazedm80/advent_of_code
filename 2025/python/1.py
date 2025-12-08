def main():
    with open("./input.txt") as f:
        lines = f.readlines()
    start = 50
    password1 = 0
    password2 = 0
    for line in lines:
        s, num = line[0], int(line[1:])
        if s == 'L':
            password2 += num // 100
            if start != 0 and (num % 100) >= start:
                password2 += 1
            start = (start - num) % 100
        else:
            start += num
            password2 += start // 100
            start = start % 100
        if start == 0:
            password1 +=1

    print(f"part 1: {password1}")
    print(f"part 2: {password2}")


if __name__ == "__main__":
    main()
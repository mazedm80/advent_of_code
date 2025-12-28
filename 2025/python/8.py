import math
from typing import List

def line_distance(p1, q1, p2, q2, p3, q3) -> float:
    d = math.sqrt((p1-q1)**2 + (p2-q2)**2 + (p3-q3)**2)
    return d

def find_circuit_pos(c: List, circuits: List) -> int:
    for i, circuit in enumerate(circuits):
        if c in circuit:
            return i
    return None

def solution(part_2: bool, junctions: List[List]):
    distances = []
    for i in range(len(junctions)):
        for j in range(i+1, len(junctions)):
            distance = line_distance(
                junctions[i][0],
                junctions[j][0],
                junctions[i][1],
                junctions[j][1],
                junctions[i][2],
                junctions[j][2]
            )
            distances.append([distance, [i, j]])
    
    distances.sort(reverse=True)
    circuits = [set([n]) for n in range(len(junctions))]

    i = 1000
    while i > 0:
        i-=1
        c1, c2 = distances.pop()[1]
        i1, i2 = find_circuit_pos(c1, circuits), find_circuit_pos(c2, circuits)
        if i1 != i2:
            circuits[i1] = circuits[i1].union(circuits[i2])
            del circuits[i2]
        if part_2:
            if len(circuits) == 1:
                break
            i+=1

    circuits.sort(key= lambda c: len(c), reverse=True)

    return circuits, c1, c2


def main():
    junctions =[]
    with open("./input.txt") as f:
        lines = f.readlines()
        junctions = [list(map(int, line.strip().split(','))) for line in lines]

    circuits, _, _ = solution(False, junctions)
    result_1 = len(circuits[0]) * len(circuits[1]) * len(circuits[2])
    circuits, c1, c2 = solution(True, junctions)
    result_2 = junctions[c1][0] * junctions[c2][0]

    print(f"part 1: {result_1}")
    print(f"part 2: {result_2}")


if __name__ == "__main__":
    main()
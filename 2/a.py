
scores_sec = { 'X': 1, 'Y' : 2, 'Z' : 3}

name2_map = { 'X' : 'R' , 'Y' : 'P', 'Z' : 'S'}
name1_map = { 'A' : 'R' , 'B' : 'P', 'C' : 'S'}
with open('a.txt') as file:
    score = 0
    for line in file:
        first, second = line.strip().split()
        
        n1 = name1_map[first]
        n2 = name2_map[second]

        score += scores_sec[second]

        if n1 == n2:
            score += 3
            continue

        if (n2 == 'P' and n1 == 'R') or (n2 == 'R' and n1 == 'S') or (n2 == 'S' and n1 == 'P'):
            score += 6


print(score)

        
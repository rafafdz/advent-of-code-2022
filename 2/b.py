
scores_sec = { 'X': 0, 'Y' : 3, 'Z' : 6}

name1_map = { 'A' : 'R' , 'B' : 'P', 'C' : 'S'}
name2_score = { 'R': 1, 'P' : 2, 'S' : 3}

loose = { 'R' : 'S', 'P' : 'R', 'S' : 'P'}
win = { v: k for k, v in loose.items() }


with open('b.txt') as file:
    score = 0
    for line in file:
        first, sec = line.strip().split()
        
        n1 = name1_map[first]

        score += scores_sec[sec]

        
        if sec == 'X': #loose
            choose = loose[n1]
        elif sec == 'Y':
            choose = n1
        else:
            choose = win[n1]

        score += name2_score[choose]


print(score)

        
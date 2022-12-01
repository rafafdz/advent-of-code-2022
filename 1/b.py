with open('b.txt') as file:
    curr = 0
    top3 = []
    for line in file:
        if line.strip() == '':
            top3.append(curr)
            top3 = list(reversed(sorted(top3)))
            top3 = top3[:3]
            curr = 0

            continue

        curr += int(line.strip())

        

print(sum(top3))
with open('a.txt') as file:
    curr = 0
    max_count = 0
    for line in file:
        if line.strip() == '':
            if curr > max_count:
                max_count = curr
            curr = 0
            continue

        curr += int(line.strip())

        

print(max_count)
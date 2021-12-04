
depths = [int(line.rstrip('\n')) for line in open('data/data.txt')]

count = 0
for idx, depth in enumerate(depths[1:]):
    # idx is one less for depths as we are iterating over depths[1:]
    if depth > depths[idx]:
        count += 1

print(count)
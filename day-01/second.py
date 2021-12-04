
depths = [int(line.rstrip('\n')) for line in open('data/data.txt')]

windows = []

for i in range(len(depths[0:-2])):
    windows.append(depths[i] + depths[i+1] + depths[i+2])


count = 0
for idx, window in enumerate(windows[1:]):
    # idx is one less for depths as we are iterating over depths[1:]
    if window > windows[idx]:
        count += 1

print(count)
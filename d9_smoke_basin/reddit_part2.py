import numpy as np
from collections import Counter
from skimage import measure

list2d = []

with open('d9_smoke_basin/smoke_input.txt', 'r') as f:
    for line in f.readlines():
        list2d.append(list(line.rstrip('\n')))

a = np.array(list2d).astype(np.int32)
b = a != 9
c = b.astype(int)
d = measure.label(c, connectivity=1)
count = Counter()
for x in range(np.max(d))[1:]:
    count[x] = np.count_nonzero(d == x)
basins = count.most_common(3)
result = 1
for x in basins:
    result = result * x[1]
print(result)
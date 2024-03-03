l=['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
frequency = {}
for item in l:
 if item in frequency:
    frequency[item] += 1
 else:
    frequency[item] = 1
print(frequency)

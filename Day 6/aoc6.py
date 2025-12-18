numrows = []
srows = []

with open("input6.txt") as f:
    for line in f:
        line = line.strip()
        if ('*' in line) or ('+' in line):
            srows.append(line)
        else:
            numrows.append([digit for digit in line])
        
results = []
for i in range(4):
    for j in range(len(numrows[i])):
        if srows[0][j] == '*':
            

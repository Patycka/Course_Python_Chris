'''
Function open(file, mode) opens file and returns file object.
File open modes:
'r' - read, returns error if file doesn't exist
'a' - append, opens file to write (add text to the file)
'w' - write - opens file to write (overwrite the content if there was one already)
'''

# read one line example
with open('test.txt', 'r') as file:
    line = file.readline()
    print(line)

# read all lines in the file example
with open('test.txt', 'r') as file:
    lines = file.readlines()
    print(lines)


# Task 1.
# Change the elements of the list "lines" so that they don't contain newlines.
with open('test.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        print(line, end=" ")

print(" ", end="\n")

# Task 2.
# Read the file mapa.txt. try to sum numbers which are in the first line.
# Test your solution (e.g. by changing number in the file)

with open('mapa.txt', 'r') as file:
    line = file.readline()
    num_str = line.strip().split(" ")
    sum_num = [int(i) for i in num_str]
    print(sum(sum_num))
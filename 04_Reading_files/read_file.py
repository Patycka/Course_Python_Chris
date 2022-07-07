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
    for index in range(len(lines)):
        lines[index] = lines[index].strip()

print(lines)

# Task 2.
# Read the file mapa.txt. try to sum numbers which are in the first line.
# Test your solution (e.g. by changing number in the file)

with open('mapa.txt', 'r') as file:
    line = file.readline()
    num_str = line.strip().split(" ")
    sum_num = [int(i) for i in num_str]
    print(sum(sum_num))

num = 12345
product = 1
while num != 0:
    last_digit = num % 10
    product = product * last_digit
    num = num // 10
print(product)

num = 123456789
total = 0
while num != 0:
    last_digit = num % 10
    if last_digit > 4:
        total += 1
    num = num // 10
print(total)

# to write some info in books.txt and read it
with open("books.txt", "w") as file:
    my_text = "The books for summer:\n'The Glass Bead Game'\n'Orientalism'\n'Social Psychology'"
    lines = file.writelines(my_text)

with open("books.txt", "r") as f:
    lines1 = f.readlines()
    lines1 = "".join(lines1) #  "because the lines1" is list
    print(lines1)


# To add items to the book list

additional_list = "\n'Quo Vadis'\n'Pan Tadeusz'"

f = open('books.txt', 'a')
f.write(additional_list)
f.close()

with open("books.txt", "a") as file:
    l = file.write(additional_list)
# ValueError: I/O operation on closed file.

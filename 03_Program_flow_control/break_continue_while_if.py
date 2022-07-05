string_number = '123456789'

# break breakss block of the code and go to another block (if exists)
for i in string_number:
    if i == "6":
        break
    print(i)

# Print at the end the new string which has only 'Python'
new_name = ""
name = "Python Course"
for a in name:
    new_name += a
    if a == " ":
        break
print(new_name)

# Validate the passowrd (find @ in the email, then break the for loop)
email = 'kowalski@gmail.com'
for j in email:
    #print("Monkey found")
    if j == "@":
        print("Monkey found")
        break

# Continue - returns to the block condition
for i in range(10):
    if i == 5 or i == 8:
        continue
    print(i)

# Task 1. Use for loop generate 20 numbers (range), print only (numbers divided by two), use continue

for i in range(1, 21):
    if i % 2 == 1:
        continue
    print("Numbers divided by two:", i)

# Task 2. hasztags = '#Python#is#simple#language' create new string variable which includes the same name but without
# hashtags, use continue

hashtag_str = "#Python#is#simple#language"
for j in hashtag_str:
    if j == "#":
        continue
    print(j, end="")
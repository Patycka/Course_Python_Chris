import requests

try:
    response = requests.get('https://www.ciach.net/python/job.45942941.json', auth=("python", "test"))
except:
    print("error 404")

print(response)

if response.status_code == 200:
    print("Success")


data_server = response.json()
print(data_server)


def get_value(key):
    return data_server[key]


def get_nested_value(key, key_nested):
    dict_nested = get_value(key)
    return dict_nested[key_nested]


print(get_value("name"))
print(get_value("duration"))
print(get_nested_value("user", "name"))

# Task 1.
# Read the second file from the server https://www.ciach.net/python/jobs.json
# Output of the script should be 2 lists, one with values of the 'id' key and
# the second one, with the values of the 'name' key.

print("\n-----------\n")

try:
    response = requests.get('https://www.ciach.net/python/jobs.json', auth=("python", "test"))
except:
    print("error 404")

if response.status_code == 200:
    print("Success")

data_server1 = response.json()
#print(data_server1)



id_list = []
name_list = []

for dictionary in data_server1:
    #print(dictionary)
   # print(row["id"])
    dict_user = dictionary["user"]
    print(dict_user["id"])

    #for i in row["user"]:
     #   print(i)
      #  #print(i["id"])
       # break



# Task 1.
# Find the library to read excel file in python and try to read example excel file.

import csv

with open("deniro.csv", newline="") as csvfile:
    reader = csv.reader(
        csvfile,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        skipinitialspace=True,
    )
    print("\nThe csv file:\n")
    print(type(reader))
    list_2 = []
    for row in reader:
        list_2.append(row)
        print(' - '.join(row))

    for item in list_2[1:]:
        for j in item[0:2]:
            int(j)
        #print(item.sort(key=item[1]))

    #list_2.sort(key=list_2[1])





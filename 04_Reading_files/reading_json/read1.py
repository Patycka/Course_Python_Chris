import requests

try:
    response = requests.get('https://www.ciach.net/python/job.45942941.json', auth = ("python", "test"))
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

# Task 1.
# Find the library to read excel file in python and try to read example excel file.
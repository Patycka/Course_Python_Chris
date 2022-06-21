stocks = {'AMZN.US': 'Amazon.com Inc',
          'GOOGL.US': 'Alphabet Inc',
          'AAPL.US': 'Apple Inc',
          'UBER.US': 'Uber Technologies Inc',
          'MSFT.US': 'Microsoft Corp'}

print(stocks.keys())

print(stocks.values())

print(stocks.items())

stocks_dict = {key: value for (key, value) in stocks.items()}
print(stocks_dict)

stocks_dict_1 = {(key, value) for (key, value) in stocks.items()}
print(stocks_dict_1)

# Change value to the key and key to the value

stocks_changed_dict = {value : key for (key, value) in stocks.items()}
print(stocks_changed_dict)

# Change keys to small letters
dict_small_keys = {key.lower(): value for (key, value) in stocks_dict.items()}
print(dict_small_keys)

# Change the values to the length current value

dict_value_length = {key: len(value.replace(" ", "")) for (key, value) in stocks_dict.items()}
print(dict_value_length)

# key: 'value:lenth()'

stocks_full_value = {key: value + ": " + str(len(value)) for (key, value) in stocks_dict.items()}
print(stocks_full_value)

nested_dict = {'001': {'price': 100},
               '002': {'price': 40},
               '003': {'price': 60}}

# print tuples of key, value
# Print only prices
# Calculate mean of the price


dict_tuples = {key: value for (key, value) in nested_dict.items()}
print(dict_tuples)
# yes, tuples!
num_lst = []
for k, i in dict_tuples.items():
    print(i)
    for values in i.values():
        num_lst.append(values)
        print(values)

dict_tuples_1 = {value['price'] for (key, value) in nested_dict.items()}


print(dict_tuples_1)
#dict_tuples = {value['price'] for (key, value) in nested_dict.items()}

list_values_2 = [value["price"] for value in nested_dict.values()]
print(list_values_2)
dict1 = {'one': 1, 'two': 2}
print(dict1["one"])

mean_num = max(num_lst) / len(num_lst)
print(mean_num)
import pandas as pd

deniro_csv = "deniro.csv"

deniro_data = pd.read_csv(deniro_csv, sep=";", decimal=".")
print(deniro_data)



#print(type(deniro_data))
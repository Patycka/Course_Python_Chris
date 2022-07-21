import pandas as pd

deniro_csv = "deniro.csv"

deniro_data = pd.read_csv(deniro_csv, sep=",", quotechar='"', skipinitialspace=True)
print(deniro_data)



#print(type(deniro_data))
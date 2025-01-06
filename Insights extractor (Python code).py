
import pandas as pd 

df = pd.read_csv(r"Paste Your file Path Here")



for column in df.columns:
    unique_values = df[column].unique()
    dtype = df[column].dtype
    if len(unique_values) > 1:
        print(f"Column: {column}")
        print(f"Data Type: {dtype}")
        print(f"Unique Values: {unique_values}\n")
        
        
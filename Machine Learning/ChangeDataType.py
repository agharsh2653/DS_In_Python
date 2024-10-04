import pandas as pd
dataset = pd.read_csv("loan.csv")
dataset.head(5)
dataset.info()
dataset.isnull().sum()
dataset["Dependents"].value_counts()

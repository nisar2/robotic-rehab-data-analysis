results_csv_pth = "results.csv"
import pandas as pd
import matplotlib.pyplot as plt

results_csv= pd.read_csv(results_csv_pth)
print(results_csv.head())
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# Set font to Times New Roman
mpl.rcParams['font.family'] = 'Times New Roman'

csv_pth = 'for_box_3.csv'
df = pd.read_csv(csv_pth)
# Create a frequency table for the 'Group' column
frequency_table = df['Group'].value_counts().reset_index()
frequency_table.columns = ['Group', 'Frequency']

# Display the frequency table
print(frequency_table)
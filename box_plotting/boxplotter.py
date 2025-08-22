import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

# Set font to Times New Roman
mpl.rcParams['font.family'] = 'Times New Roman'

csv_pth = 'for_box_3.csv'
df = pd.read_csv(csv_pth)
df = df[df['Group'] != 'Healthy Assisted']

# # Label group
# def label_group(row):
#     if row['DIAGNOSIS'] == 'Healthy' and not row['ASSISTANCE']:
#         return 'Healthy Unassisted'
#     elif row['DIAGNOSIS'] != 'Healthy' and row['ASSISTANCE']:
#         return 'Patient Assisted'
#     elif row['DIAGNOSIS'] != 'Healthy' and not row['ASSISTANCE']:
#         return 'Patient Unassisted'
#     else:
#         return None

# # Preprocessing
# df['AVERAGE DEVIATION (cm) '] = df['AVERAGE DEVIATION (cm) '] * 10
# df['Group'] = df.apply(label_group, axis=1)
# df_filtered = df.dropna(subset=['Group'])

# Plotting
# Set fonts and sizes
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.size'] = 14  # base font size
mpl.rcParams['axes.titlesize'] = 18
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['legend.fontsize'] = 13

# Plot
plt.figure(figsize=(8, 5))  # smaller figsize for tighter layout in Word

sns.boxplot(
    data=df,
    x='SHAPE',
    y='AVERAGE DEVIATION (mm) ',
    hue='Group',
    order=['Hexagon', 'Triangle', 'Circle', 'Infinity', 'B'],
    dodge=True,
    width=0.5,
    linewidth=2,       # ✅ thicker lines
    fliersize=4        # slightly larger outliers
)
# Set custom legend labels
handles, labels = plt.gca().get_legend_handles_labels()
custom_labels = ['Healthy', 'Patient Assisted', 'Patient Unassisted']
plt.legend(handles, custom_labels, title=None, loc='upper left', bbox_to_anchor=(0, 1), frameon=True)

# Grid lines
ax = plt.gca()
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
ax.grid(which='major', axis='y', linestyle='--', linewidth=1.2, alpha=0.6, color='gray')
# ax.grid(which='minor', axis='y', linestyle=':', linewidth=1.0, alpha=0.4, color='gray')
ax.grid(which='major', axis='x', linestyle='--', linewidth=1.2, alpha=0.6, color='gray')

# Manual minor x-grid midpoints if needed...
# [same as before]

# Axis labels and title
# plt.title('Deviation by Shape and Group', fontsize=18)
plt.xlabel('')  # remove x label
plt.ylabel('Average Deviation (mm)', fontsize=16)

# Legend
# plt.legend(title=None, loc='upper right', bbox_to_anchor=(1, 1), frameon=True)

# ✅ Save with high DPI and tight layout
plt.tight_layout(pad=2)
plt.savefig('box_plot_deviation_wo_healthy_assisted.svg', bbox_inches='tight')
plt.savefig('box_plot_deviation_wo_healthy_assisted.png', bbox_inches='tight', dpi=600)


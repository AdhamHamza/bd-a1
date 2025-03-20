import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import subprocess

input_file = "/home/doc-bd-a1/res_dpre.csv"
df = pd.read_csv(input_file)
print(df.head())          
plt.figure(figsize=(8, 6))
sns.histplot(df[df.columns[1]], bins=20, kde=False)
plt.title("Distribution of Survived column")
plt.savefig("vis.png")

print("Visualization saved as vis.png.")

# Call the next script (model.py)
subprocess.run(["python3", "model.py", input_file])
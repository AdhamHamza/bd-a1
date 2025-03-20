import pandas as pd
import subprocess
# Load the preprocessed dataset
df = pd.read_csv("/home/doc-bd-a1/res_dpre.csv")

# EDA 'insights'
insight1 = f"Mean of column Age: {df['Age'].mean()}"
insight2 = f"Median of column Fare: {df['Fare'].median()}"
insight3 = f"Standard deviation of column Age: {df['Age'].std()}"

# Save insights to text files
with open("/home/doc-bd-a1/eda-in-1.txt", "w") as f:
    f.write(insight1)
with open("/home/doc-bd-a1/eda-in-2.txt", "w") as f:
    f.write(insight2)
with open("/home/doc-bd-a1/eda-in-3.txt", "w") as f:
    f.write(insight3)
subprocess.run(["python3", "vis.py", "/home/doc-bd-a1/res_dpre.csv"])
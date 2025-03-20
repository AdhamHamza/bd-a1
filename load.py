import sys
import pandas as pd
import subprocess
dataset_path = sys.argv[1]
df = pd.read_csv(dataset_path)
print("Dataset loaded successfully!")
# Pass the dataframe to the next script
df.to_csv("/home/doc-bd-a1/res_load.csv", index=False)
subprocess.run(["python3", "dpre.py", "/home/doc-bd-a1/res_load.csv"])
import pandas as pd
import numpy as np

# === Load dataset ===
df = pd.read_csv("shape_dataset.csv")
df = df.sample(n=100, random_state=42).reset_index(drop=True)  # 100 random samples

X = df.drop('label', axis=1).values
y = df['label'].values

# === Save inputs in Verilog-style .mem format
with open("test_inputs.mem", "w") as f_in:
    for row in X:
        bits = ''.join(str(b) for b in row)
        f_in.write(f"{int(bits, 2):016X}\n")  # Write 64-bit hex per line

# === Save labels
with open("labels.mem", "w") as f_label:
    for label in y:
        f_label.write(f"{label}\n")

print("✅ Exported 100 test samples to test_inputs.mem and labels.mem")

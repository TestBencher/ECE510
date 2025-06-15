import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# === 1. Load Dataset ===
df = pd.read_csv('shape_dataset_claude.csv')
X = df.drop('label', axis=1).values
y = df['label'].values

# === 2. Train/Test Split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === 3. Train Logistic Regression (Softmax) ===
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X_train, y_train)

# === 4. Evaluate Floating-Point Accuracy ===
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n✅ Accuracy on test set: {acc*100:.2f}%")
print(classification_report(y_test, y_pred))

# === 5. Quantize Weights and Biases to Q4.4 ===
W_float = model.coef_   # Shape: (3, 64)
B_float = model.intercept_

W_fixed = np.round(W_float * 16).astype(int)
B_fixed = np.round(B_float * 16).astype(int)

np.savetxt("weights_fixed.csv", W_fixed, fmt="%d", delimiter=",")
np.savetxt("biases_fixed.csv", B_fixed.reshape(1, -1), fmt="%d", delimiter=",")

print("✅ Saved weights_fixed.csv and biases_fixed.csv (Q4.4 format)")

# === 6. Generate Verilog Initial Block ===
with open("verilog_initial_block.v", "w") as f:
    f.write("// Auto-generated Verilog initial block (Q4.4)\n")
    f.write("initial begin\n")

    flat_w = W_fixed.flatten()
    for i, val in enumerate(flat_w):
        sign = '-' if val < 0 else ''
        f.write(f"    W[{i}] = {sign}8'sd{abs(val)};\n")

    f.write("\n")
    for i, val in enumerate(B_fixed):
        sign = '-' if val < 0 else ''
        f.write(f"    BIAS[{i}] = {sign}16'sd{abs(val)};\n")

    f.write("end\n")
print("✅ Verilog initial block written to verilog_initial_block.v")

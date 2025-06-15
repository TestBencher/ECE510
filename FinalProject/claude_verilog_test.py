import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# === 1. Load full dataset ===
df = pd.read_csv("shape_dataset_claude.csv")
X = df.drop('label', axis=1).values
y = df['label'].values

# === 2. Train on all 1000 samples ===
model = LogisticRegression(solver='lbfgs', max_iter=1000)
model.fit(X, y)

# === 3. Evaluate training accuracy ===
y_pred = model.predict(X)
acc = accuracy_score(y, y_pred)
print(f"\n✅ Accuracy on full dataset (training): {acc*100:.2f}%")
print(classification_report(y, y_pred))

# === 4. Quantize weights/biases to Q4.4 ===
W_float = model.coef_
B_float = model.intercept_

W_fixed = np.round(W_float * 16).astype(int)
B_fixed = np.round(B_float * 16).astype(int)

np.savetxt("weights_fixed.csv", W_fixed, fmt="%d", delimiter=",")
np.savetxt("biases_fixed.csv", B_fixed.reshape(1, -1), fmt="%d", delimiter=",")
print("✅ Saved weights_fixed.csv and biases_fixed.csv")

# === 5. Export 100 test vectors and labels as .mem ===
X_sample = X[:100]
y_sample = y[:100]

with open("test_inputs.mem", "w") as f_in:
    for row in X_sample:
        bits = ''.join(str(int(b)) for b in row)
        f_in.write(f"{int(bits, 2):016X}\n")

with open("labels.mem", "w") as f_label:
    for label in y_sample:
        f_label.write(f"{label}\n")


print("✅ Exported test_inputs.mem and labels.mem (100 samples)")

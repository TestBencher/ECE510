import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("shape_dataset.csv")
X = df.drop('label', axis=1).values  # binary edge maps
y_true = df['label'].values          # ground truth labels

# Load fixed-point model
W = np.loadtxt("weights_fixed.csv", delimiter=",", dtype=int)
B = np.loadtxt("biases_fixed.csv", delimiter=",", dtype=int).flatten()

# Inference loop
correct = 0
for idx, x in enumerate(X):
    scores = []
    for c in range(3):
        score = B[c]
        for i in range(64):
            if x[i]:
                score += W[c][i]
        scores.append(score)
    y_pred = np.argmax(scores)
    if y_pred == y_true[idx]:
        correct += 1

accuracy = (correct / len(X)) * 100
print(f"✅ Software fixed-point model accuracy: {accuracy:.2f}% ({correct}/{len(X)})")

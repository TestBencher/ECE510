import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
import joblib

# === Load Dataset ===
df = pd.read_csv('shape_dataset.csv')
X = df.drop('label', axis=1).values  # Shape: (samples, 64)
y = df['label'].values               # Shape: (samples,)

# === Split into Train/Test ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Train Logistic Regression (Softmax) ===
model = LogisticRegression(
    multi_class='multinomial',  # Softmax classifier
    solver='lbfgs',
    max_iter=1000
)
model.fit(X_train, y_train)

# === Evaluate ===
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# === Save Model ===
joblib.dump(model, 'shape_logistic_model.pkl')
print("✅ Model saved as shape_logistic_model.pkl")

# === Export Weights (for Verilog)
W = model.coef_  # Shape: (3 classes, 64 features)
b = model.intercept_  # Shape: (3,)

np.savetxt("weights.csv", W, delimiter=',', fmt="%.6f")
np.savetxt("biases.csv", b.reshape(1, -1), delimiter=',', fmt="%.6f")
print("✅ Weights and biases exported to weights.csv and biases.csv")

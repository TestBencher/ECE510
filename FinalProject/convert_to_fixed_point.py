import numpy as np

# === Load Weights and Biases ===
W = np.loadtxt('weights.csv', delimiter=',')
b = np.loadtxt('biases.csv', delimiter=',')

# === Convert to Q4.4 Fixed-Point ===
scale = 16  # 2^4
W_fixed = np.round(W * scale).astype(int)
b_fixed = np.round(b * scale).astype(int)

# === Save as Fixed-Point CSV ===
np.savetxt("weights_fixed.csv", W_fixed, fmt="%d", delimiter=",")
np.savetxt("biases_fixed.csv", b_fixed.reshape(1, -1), fmt="%d", delimiter=",")

print("✅ Fixed-point weights saved to weights_fixed.csv")
print("✅ Fixed-point biases saved to biases_fixed.csv")

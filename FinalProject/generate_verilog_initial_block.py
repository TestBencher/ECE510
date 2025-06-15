import numpy as np

# === Load fixed-point weights and biases ===
W = np.loadtxt("weights_fixed.csv", delimiter=",", dtype=int)
B = np.loadtxt("biases_fixed.csv", delimiter=",", dtype=int).flatten()

with open("verilog_initial_block.v", "w") as f:
    f.write("// Auto-generated initial block for shape_classifier.v\n")
    f.write("initial begin\n\n")

    # Flatten weights and format as signed Verilog literals
    W_flat = W.flatten()
    for i, w in enumerate(W_flat):
        sign = '-' if w < 0 else ''
        f.write(f"    W[{i}] = {sign}8'sd{abs(w)};\n")

    f.write("\n")

    # Biases
    for i, b in enumerate(B):
        sign = '-' if b < 0 else ''
        f.write(f"    BIAS[{i}] = {sign}16'sd{abs(b)};\n")

    f.write("end\n")

print("✅ Verilog initial block saved as verilog_initial_block.v")

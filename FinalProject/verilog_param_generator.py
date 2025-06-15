import numpy as np

# === Load fixed-point weights and biases ===
W = np.loadtxt('weights_fixed.csv', delimiter=',', dtype=int)
B = np.loadtxt('biases_fixed.csv', delimiter=',', dtype=int).flatten()

# === Flatten W: concatenate all rows
W_flat = W.flatten()

# === Write to file
with open("verilog_weights.vh", "w") as f:
    f.write("// Auto-generated flattened weights and biases in fixed-point (Q4.4)\n\n")

    f.write("localparam signed [7:0] W [0:192] = '{\n")
    for i, val in enumerate(W_flat):
        f.write(f"    {val:+d}" + (",\n" if i < len(W_flat) - 1 else "\n"))
    f.write("};\n\n")

    f.write("localparam signed [15:0] BIAS [0:2] = '{")
    f.write(", ".join([f"{val:+d}" for val in B]))
    f.write("};\n")

print("✅ Flattened Verilog weights saved as verilog_weights_flat.vh")

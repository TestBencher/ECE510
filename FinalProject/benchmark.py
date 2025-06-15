import numpy as np
import time

# === Load fixed-point model ===
W = np.loadtxt("weights_fixed.csv", delimiter=',', dtype=int)
B = np.loadtxt("biases_fixed.csv", delimiter=',', dtype=int).flatten()

# === Define test shapes (8×8 flattened edge maps)
shape_images = [
    # Square
    [
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,
        0,0,1,1,1,1,0,0,
        0,0,1,0,0,1,0,0,
        0,0,1,0,0,1,0,0,
        0,0,1,1,1,1,0,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0
    ],
    # Circle
    [
        0,0,0,0,0,0,0,0,
        0,0,0,1,1,0,0,0,
        0,0,1,1,1,1,0,0,
        0,1,1,1,1,1,1,0,
        0,1,1,1,1,1,1,0,
        0,0,1,1,1,1,0,0,
        0,0,0,1,1,0,0,0,
        0,0,0,0,0,0,0,0
    ],
    # Triangle
    [
        0,0,0,0,0,0,0,0,
        0,0,0,1,0,0,0,0,
        0,0,1,1,1,0,0,0,
        0,1,1,1,1,1,0,0,
        1,1,1,1,1,1,1,0,
        0,0,1,1,1,0,0,0,
        0,0,0,1,0,0,0,0,
        0,0,0,0,0,0,0,0
    ]
]

# === Run benchmark ===
num_shapes = len(shape_images)
runs_per_shape = 1000
total_runs = num_shapes * runs_per_shape

start = time.time()

for _ in range(runs_per_shape):
    for x in shape_images:
        scores = []
        for c in range(3):
            score = B[c]
            for i in range(64):
                if x[i]:
                    score += W[c][i]
            scores.append(score)
        pred = np.argmax(scores)

end = time.time()

total_time = end - start
avg_time_us = (total_time / total_runs) * 1e6

print(f"✅ Average software inference time over {total_runs} runs: {avg_time_us:.2f} µs")

import numpy as np

# Load Q4.4 fixed-point weights & biases
W = np.loadtxt('weights_fixed.csv', delimiter=',', dtype=int)
B = np.loadtxt('biases_fixed.csv', delimiter=',', dtype=int).flatten()

circle_image = [
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,1,1,1,1,0,0,
    0,0,1,0,0,1,0,0,
    0,0,1,0,0,1,0,0,
    0,0,1,1,1,1,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0
]


# Flattened test input (same as shape_mem[1])
x = np.array(circle_image)

# Perform fixed-point dot product
scores = []
for c in range(3):
    score = B[c]
    for i in range(64):
        if x[i]:
            score += W[c][i]
    scores.append(score)

pred_class = np.argmax(scores)
print("Predicted class:", pred_class)  # Expect: 2 → circle

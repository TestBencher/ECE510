import numpy as np
import cv2
import csv
import random
from PIL import Image, ImageDraw

# === Config ===
IMG_SIZE = 32        # Start large and downsample to 8×8
TARGET_SIZE = 8
SHAPES = ['triangle', 'square', 'circle']
SAMPLES_PER_CLASS = 200

def draw_shape(shape, img_size):
    img = Image.new('L', (img_size, img_size), 0)
    draw = ImageDraw.Draw(img)
    if shape == 'circle':
        r = random.randint(8, 12)
        cx, cy = img_size//2, img_size//2
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=255)
    elif shape == 'square':
        s = random.randint(14, 18)
        x0 = (img_size - s) // 2
        draw.rectangle((x0, x0, x0 + s, x0 + s), fill=255)
    elif shape == 'triangle':
        w = random.randint(16, 20)
        h = w
        cx, cy = img_size//2, img_size//2 + 3
        pts = [(cx, cy - h//2), (cx - w//2, cy + h//2), (cx + w//2, cy + h//2)]
        draw.polygon(pts, fill=255)
    return np.array(img)

def process_image(img):
    blurred = cv2.GaussianBlur(img, (3, 3), 0)
    edges = cv2.Canny(blurred, 50, 150)
    downsampled = cv2.resize(edges, (TARGET_SIZE, TARGET_SIZE), interpolation=cv2.INTER_NEAREST)
    binary = (downsampled > 0).astype(np.uint8)
    return binary.flatten()

# === Generate Dataset ===
data = []
labels = []

for label, shape in enumerate(SHAPES):
    for _ in range(SAMPLES_PER_CLASS):
        img = draw_shape(shape, IMG_SIZE)
        edge_map = process_image(img)
        data.append(edge_map.tolist())
        labels.append(label)

# === Save as CSV ===
with open('shape_dataset.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['pixel' + str(i) for i in range(TARGET_SIZE * TARGET_SIZE)] + ['label'])
    for x, y in zip(data, labels):
        writer.writerow(x + [y])

print("✅ Dataset generated: shape_dataset.csv")

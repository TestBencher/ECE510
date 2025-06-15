import numpy as np
import pandas as pd
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def create_empty_image():
    """Create an empty 8x8 binary image."""
    return np.zeros((8, 8), dtype=int)

def draw_circle(img, radius=None, center=None):
    """Draw a circle edge on the image."""
    if radius is None:
        radius = random.uniform(2.0, 3.0)
    if center is None:
        # Slightly off-center positions for variety
        center = (random.uniform(3.0, 4.5), random.uniform(3.0, 4.5))
    
    for i in range(8):
        for j in range(8):
            # Calculate distance from center
            distance = np.sqrt((i - center[0])**2 + (j - center[1])**2)
            # Mark pixels that are close to the circle edge
            if abs(distance - radius) < 0.5:
                img[i, j] = 1
    
    return img

def draw_square(img, size=None, position=None):
    """Draw a square edge on the image."""
    if size is None:
        size = random.uniform(3.0, 5.0)
    if position is None:
        # Slightly off-center positions for variety
        position = (random.uniform(1.5, 2.5), random.uniform(1.5, 2.5))
    
    x, y = position
    half_size = size / 2
    
    # Draw the four edges of the square
    for i in range(8):
        for j in range(8):
            # Top edge
            if abs(i - x) < 0.5 and y <= j <= y + size:
                img[i, j] = 1
            # Bottom edge
            elif abs(i - (x + size)) < 0.5 and y <= j <= y + size:
                img[i, j] = 1
            # Left edge
            elif abs(j - y) < 0.5 and x <= i <= x + size:
                img[i, j] = 1
            # Right edge
            elif abs(j - (y + size)) < 0.5 and x <= i <= x + size:
                img[i, j] = 1
    
    return img

def draw_triangle(img, size=None, position=None):
    """Draw a triangle edge on the image."""
    if size is None:
        size = random.uniform(4.0, 5.5)
    if position is None:
        # Position the triangle within the image
        position = (random.uniform(1.5, 2.5), random.uniform(1.5, 2.5))
    
    x, y = position
    
    # Define the three vertices of the triangle
    # We'll create an equilateral triangle
    x1, y1 = x + size/2, y  # Top vertex
    x2, y2 = x, y + size    # Bottom left vertex
    x3, y3 = x + size, y + size  # Bottom right vertex
    
    # Draw the three edges of the triangle using line drawing algorithm
    for i in range(8):
        for j in range(8):
            # Check if point is close to any of the three edges
            # Edge 1: from vertex 1 to vertex 2
            d1 = point_to_line_distance(i, j, x1, y1, x2, y2)
            # Edge 2: from vertex 2 to vertex 3
            d2 = point_to_line_distance(i, j, x2, y2, x3, y3)
            # Edge 3: from vertex 3 to vertex 1
            d3 = point_to_line_distance(i, j, x3, y3, x1, y1)
            
            # If point is close to any edge, mark it
            if min(d1, d2, d3) < 0.5:
                img[i, j] = 1
    
    return img

def point_to_line_distance(x, y, x1, y1, x2, y2):
    """Calculate the distance from point (x,y) to line segment (x1,y1)-(x2,y2)."""
    # Vector from point 1 to point 2
    line_vec = np.array([x2-x1, y2-y1])
    # Vector from point 1 to the point
    pnt_vec = np.array([x-x1, y-y1])
    # Unit vector of the line
    line_len = np.linalg.norm(line_vec)
    line_unitvec = line_vec / line_len if line_len > 0 else np.array([0, 0])
    
    # Project pnt_vec onto line_unitvec
    pnt_vec_proj = np.dot(pnt_vec, line_unitvec)
    
    # If projection is outside the line segment, use distance to the nearest endpoint
    if pnt_vec_proj < 0:
        return np.linalg.norm(pnt_vec)
    elif pnt_vec_proj > line_len:
        return np.linalg.norm(np.array([x-x2, y-y2]))
    else:
        # Distance to line is the norm of the rejection
        return np.linalg.norm(pnt_vec - line_unitvec * pnt_vec_proj)

def generate_shape_datasets(num_samples=1000):
    """Generate binary shape datasets with approximately equal distribution."""
    # Determine the number of samples for each shape
    shape_counts = {
        "triangle": num_samples // 3,
        "square": num_samples // 3,
        "circle": num_samples - (2 * (num_samples // 3))  # Ensure we have exactly num_samples
    }
    
    features = []
    labels = []
    
    # Generate samples for each shape type
    for shape_type, count in shape_counts.items():
        for _ in range(count):
            img = create_empty_image()
            
            if shape_type == "circle":
                img = draw_circle(img)
                label = 2
            elif shape_type == "square":
                img = draw_square(img)
                label = 1
            else:  # triangle
                img = draw_triangle(img)
                label = 0
            
            # Flatten the image to a 1D array (row-major order)
            flattened = img.flatten()
            features.append(flattened)
            labels.append(label)
    
    # Combine features and labels
    X = np.array(features)
    y = np.array(labels)
    
    # Shuffle the dataset
    indices = np.arange(len(y))
    np.random.shuffle(indices)
    X = X[indices]
    y = y[indices]
    
    return X, y

def create_and_save_dataset(num_samples=1000, output_file="shape_dataset_claude.csv"):
    """Create and save the shape dataset to a CSV file."""
    X, y = generate_shape_datasets(num_samples)
    
    # Create feature column names (f0 to f63)
    feature_cols = [f"f{i}" for i in range(64)]
    
    # Create DataFrame
    df = pd.DataFrame(X, columns=feature_cols)
    df["label"] = y
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    
    return df

# Generate the dataset
shape_df = create_and_save_dataset(1000, "shape_dataset_claude.csv")

# Display some statistics
print(f"Dataset shape: {shape_df.shape}")
print(f"Label distribution: {shape_df['label'].value_counts().sort_index()}")

# Display a few examples
print("\nSample data (first 5 rows):")
print(shape_df.head())

# Create a function to visualize a few samples (this won't run in the artifact, 
# but would be useful if you want to verify the shapes)
def visualize_sample(row_idx):
    """Visualize a shape from the dataset."""
    row = shape_df.iloc[row_idx]
    img = row[:-1].values.reshape(8, 8)
    label_map = {0: "Triangle", 1: "Square", 2: "Circle"}
    label = label_map[row["label"]]
    
    print(f"Shape: {label}")
    for i in range(8):
        print("".join(["■" if img[i, j] == 1 else "□" for j in range(8)]))
    print()

# Function to get some examples of each shape class
def print_examples_for_each_class():
    """Print examples of each shape class."""
    for class_label in [0, 1, 2]:
        class_indices = shape_df[shape_df["label"] == class_label].index[:2]
        for idx in class_indices:
            visualize_sample(idx)

# Get the CSV content as a string
csv_content = shape_df.to_csv(index=False)

# Print the first 5 rows of the CSV content
print("\nFirst few lines of the CSV:")
print("\n".join(csv_content.split("\n")[:6]))

# Print dataset summary
print(f"\nTotal number of samples: {len(shape_df)}")
print(f"Number of features: {len(shape_df.columns) - 1}")
print(f"Number of triangles: {len(shape_df[shape_df['label'] == 0])}")
print(f"Number of squares: {len(shape_df[shape_df['label'] == 1])}")
print(f"Number of circles: {len(shape_df[shape_df['label'] == 2])}")
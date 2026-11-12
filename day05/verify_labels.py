
from pathlib import Path

# Location of the active label file
active_path = Path("labels/candidate_active.txt")

# Read the YOLO line from the text file
loaded_line = active_path.read_text().strip()

# Extract the five YOLO values
class_id, cx, cy, width, height = map(float, loaded_line.split())

# Original image dimensions
W = 8
H = 8

# Convert YOLO coordinates back to bounding box coordinates
x1 = (cx - width / 2) * W
y1 = (cy - height / 2) * H
x2 = (cx + width / 2) * W
y2 = (cy + height / 2) * H

# Create the bounding box
box = (round(x1), round(y1), round(x2), round(y2))

print("Recovered bounding box:", box)

# Verify the bounding box
assert box == (4, 0, 8, 8)

print("Bounding box verification successful!")

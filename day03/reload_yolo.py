
from pathlib import Path


def xyxy_to_yolo(box, width, height, class_id):
    left, top, right, bottom = box

    bw = right - left
    bh = bottom - top

    cx = left + bw / 2
    cy = top + bh / 2

    return (
        f"{class_id} "
        f"{cx / width:.6f} "
        f"{cy / height:.6f} "
        f"{bw / width:.6f} "
        f"{bh / height:.6f}"
    )


def yolo_to_xyxy(line, width, height):
    class_id, cx, cy, bw, bh = line.split()

    cx, cy, bw, bh = (
        float(v) for v in (cx, cy, bw, bh)
    )

    cx *= width
    cy *= height
    bw *= width
    bh *= height

    left = cx - bw / 2
    top = cy - bh / 2

    return int(class_id), (
        left, top, left + bw, top + bh
    )


def main():
    labels_dir = Path(__file__).parent / "labels"
    width = 100
    height = 100

    # Step 1: Original xyxy box -> YOLO format
    original_box = (10, 20, 50, 60)

    yolo_line = xyxy_to_yolo(
        original_box, width, height, class_id=1
    )

    print("YOLO format:", yolo_line)

    # Step 2: Save the YOLO format into a text file
    example_file = labels_dir / "example_100.txt"
    example_file.write_text(yolo_line + "\n")

    # Step 3: Read the YOLO file
    line = example_file.read_text().strip()

    # Step 4: YOLO format -> Original xyxy box
    class_id, recovered_box = yolo_to_xyxy(
        line, width, height
    )
    # Create labels directory if it doesn't exist
    labels_dir.mkdir(parents=True, exist_ok=True)

    # Row a: matched box
    a_box = (0, 0, 2, 2)

    a_yolo_line = xyxy_to_yolo(
    a_box, width, height, class_id=1
    )

    (labels_dir / "a.txt").write_text(a_yolo_line + "\n")


    # Row c: no_positive, so create an empty file
    (labels_dir / "c.txt").write_text("")

    print("Recovered class:", class_id)
    print("Recovered box:", recovered_box)


if __name__ == "__main__":
    main()

""" 
Verification done:

YOLO format: 1 0.300000 0.400000 0.400000 0.400000
Recovered class: 1
Recovered box: (10.0, 20.0, 50.0, 60.0)
"""
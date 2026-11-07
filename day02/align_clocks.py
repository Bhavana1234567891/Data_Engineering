
import csv
from pathlib import Path

import cv2

FPS = 30
OFFSET_SECONDS = 0.2
TIMES = [0.5, 1.0, 1.5]
SOURCE_ID = "clip_a"


def frame_index(timestamp: float, offset: float, fps: int) -> int:
    return int(round((timestamp + offset) * fps))


def main() -> None:
    root = Path(__file__).resolve().parent
    video_path = root / "clip_a.mp4"

    capture = cv2.VideoCapture(str(video_path))

    if not capture.isOpened():
        raise RuntimeError(f"cannot open {video_path}")

    panels = []
    rows = []

    for timestamp in TIMES:

        naive = frame_index(timestamp, 0.0, FPS)
        corrected = frame_index(timestamp, OFFSET_SECONDS, FPS)

        for kind, index in (("naive", naive), ("corrected", corrected)):

            # 1. Ask OpenCV to go to the expected frame
            capture.set(cv2.CAP_PROP_POS_FRAMES, index)

            # 2. Read that frame
            ok, image = capture.read()

            if not ok:
                raise RuntimeError(f"failed to read frame {index}")

            # 3. Get OpenCV's position AFTER reading
            reported_position = capture.get(
                cv2.CAP_PROP_POS_FRAMES
            )

            # 4. Create the white label
            label = f"{kind} t={timestamp} f={index}"

            cv2.putText(
                image,
                label,
                (8, 170),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.4,
                (255, 255, 255),
                1
            )

            panels.append(image)

            # 5. Store verification information
            rows.append({
                "source_id": SOURCE_ID,
                "ann_time": timestamp,
                "kind": kind,
                "offset_seconds": (
                    OFFSET_SECONDS if kind == "corrected" else 0.0
                ),
                "expected_frame": index,
                "rectangle_x_expected": index,
                "label": label,
                "opencv_position_after_read": reported_position,
                "read_success": ok
            })

            # 6. Print details in terminal
            print(f"\n{kind.upper()} | Annotation time: {timestamp}")
            print("Expected frame:", index)
            print("Rectangle x-position (expected):", index)
            print("Label:", label)
            print("OpenCV position after read:", reported_position)
            print("Read successful:", ok)

    capture.release()

    # Create contact sheet
    sheet = cv2.hconcat(panels)
    cv2.imwrite(str(root / "contact_sheet.png"), sheet)

    # Save original timestamp information
    with (root / "time_offset.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0].keys())
        )
        writer.writeheader()
        writer.writerows(rows)

    # Save additional verification information
    with (root / "frame_verification.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0].keys())
        )
        writer.writeheader()
        writer.writerows(rows)

    print("\nCreated contact_sheet.png")
    print("Created time_offset.csv")
    print("Created frame_verification.csv")


if __name__ == "__main__":
    main()
